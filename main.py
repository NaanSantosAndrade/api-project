from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
import openai

# Configurando dependências
app = FastAPI()
openai.api_key = "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"

# Banco de dados
trainers = {}

# Base Models
class User(BaseModel):
    name: str
    age: int
    pokemons: list
    
# Funções
def valid_trainer(trainer_id):
    valid = True if trainer_id in trainers else None
    return valid

def valid_trainer_pokemon(trainer_id, pokemon_name):
    valid = None
    
    if trainer_id in trainers:
        valid = True if pokemon_name in trainers[trainer_id]['pokemons'] else None
    
    return valid

# GET
@app.get("/list-trainers/", response_model=List[User])
def list_trainers():
    return list(trainers.values())

@app.get("/trainer_details/{trainer_id}")
def list_pokemons(trainer_id: str):
    return trainers[trainer_id]
    
@app.get("/ai_analise_pokemon/{trainer_id}/{pokemon_name}")
def ai_analise_pokemon(trainer_id: str, pokemon_name: str):
    
    trainer_name = trainers[trainer_id]['name'] if valid_trainer(trainer_id) else None
    valid_pokemon = valid_trainer_pokemon(trainer_id, pokemon_name)
    
    print("treinador: ", trainer_name)
    print("pokemon: ", valid_pokemon)
    
    if (trainer_name != None and valid_pokemon == True):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {
                    "role": "system", 
                    "content": "Você é o professor Carvalho, treinador pokemon, e gosta de explicar tudo sobre pokemons."},
                {
                    "role": "user", 
                    "content": f"Crie uma mensagem para o treinador pokemon {trainer_name} sobre as vantagens, desvantagens do pokemon {pokemon_name} e uma curiosidade sobre o pokemon. (máximo de 100 caracteres)"
                }
            ]
        )
        
        return completion.choices[0].message.content.strip('\"')
    
    if(trainer_name != None and valid_pokemon == None):
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f"Este treinador não possui o pokemon {pokemon_name}."
        )
    
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f"Treinador não encontrado."
    )

# POST
@app.post("/create-trainer/")
def create_user(user: User):
    treinador_id = str(len(trainers) + 1)
    trainers[treinador_id] = user
    return {"user_id": treinador_id, "user": user}

# PUT
# # TODO - método PUT
@app.put("/update-pokemon-group/{trainer_id}/")
def update_user(trainer_id: str, user: User):
    if trainer_id in trainers:
        existing_user = trainers[trainer_id]
        existing_user.name = user.name
        existing_user.age = user.age
        existing_user.pokemons = user.pokemons
        return {'message': f'Usuário {trainer_id} atualizado'}
    else:
        trainers[trainer_id] = user
        return {'message': f'Usuário {trainer_id} criado'}
   
    


# DELETE
@app.delete("/delete-trainer/{trainer_id}")
def delete_user(trainer_id: str):
    if trainer_id in trainers:
        del trainers[trainer_id]
        return {"status": "success", "message": "Treinador removido com sucesso"}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )



uvicorn.run(app, host="0.0.0.0", port=8000)