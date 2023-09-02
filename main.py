from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List
import uvicorn
import openai
import csv

# Configurando dependências
app = FastAPI()
openai.api_key = ""

# Banco de dados
trainers = {}

# Base Models
class User(BaseModel):
    name: str
    age: int
    pokemons: list
    
class TokenModel(BaseModel):
    token: str
    
# Funções
def check_pokemon(pokemon_name):
    with open('database.csv', 'r') as csvfile:
        dataframe = csv.DictReader(csvfile)
        for row in dataframe:
            if row['Name'] == pokemon_name:
                return True
        return None

# GET
@app.get("/list-trainers/", response_model=List[User])
def list_trainers():
    return list(trainers.values())

@app.get("/trainer_details/{trainer_id}")
def list_pokemons(trainer_id: str):
    return trainers[trainer_id]

@app.get("/pokemon_details/{pokemon_name}")
def pokemon_details(pokemon_name: str):
    if(check_pokemon(pokemon_name)):
        with open('database.csv', 'r') as csvfile:
            dataframe = csv.DictReader(csvfile)
            for row in dataframe:
                if row['Name'] == pokemon_name:
                    return row
            return None
    
@app.get("/ai_analise_pokemon/{pokemon_name}")
def ai_pokemon_analise(pokemon_name: str):
    if (check_pokemon(pokemon_name) == True):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                    {
                        "role": "system", 
                        "content": "Você é o professor Carvalho, treinador pokemon, e gosta de explicar tudo sobre pokemons."},
                    {
                        "role": "user", 
                        "content": f"Crie uma mensagem para o treinador pokemon sobre as vantagens, desvantagens do pokemon {pokemon_name} e uma curiosidade sobre o pokemon. (máximo de 100 caracteres)"
                    }
                ]
            )
            
        return completion.choices[0].message.content.strip('\"')

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pokemon não encontrado"
    )

# POST
@app.post("/change-openai-token/", response_model=None)
def change_openai_token(token_model: TokenModel):
    new_token = token_model.token
    openai.api_key = new_token
    return {"token": new_token}

@app.post("/create-trainer/")
def create_trainer(user: User):
    treinador_id = str(len(trainers) + 1)
    trainers[treinador_id] = user
    return {"user_id": treinador_id, "user": user}

# PUT
@app.put("/update-pokemon-group/{trainer_id}/")
def update_user(trainer_id: str, user: User):
    if trainer_id in trainers:
        existing_user = trainers[trainer_id]
        
        name = user.name
        age = user.age
        pokemons = user.pokemons
        
        if(name != "" and age > 5):
            existing_user.name = user.name
            existing_user.age = user.age
            
            valid_pokemons = True
            for pokemon in pokemons:
                if (check_pokemon(pokemon) == None):
                    valid_pokemons = None
            
            if (valid_pokemons):
                existing_user.pokemons = user.pokemons
                return {'message': f'Treinador {trainer_id} atualizado'}
            
            return {'error': f'Lista de Pokemons inválida.'}
        
        return {'error': f'Nome de usuário ou Idade inválido'}
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

uvicorn.run(app, host="0.0.0.0", port=80)