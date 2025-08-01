import requests
import json

URL = "https://jsonplaceholder.typicode.com"

def obtener_posts_usuario(userid):
    """Obtiene los posts de un usuario específico."""
    url = f"{URL}/posts"
    params = {'userId': userid}
    response = requests.get(url, params=params)
    posts = response.json()
    print(f"Posts del usuario {userid}:")
    for post in posts:
        print(f"- {post['title']}")
    print()

def agregar_post(titulo, cuerpo, userid):
    """Agrega un nuevo post para un usuario específico."""
    url = f"{URL}/posts"
    data = {
        "title": titulo,
        "body": cuerpo,
        "userId": userid
    }
    response = requests.post(url, json=data)
    print("Nuevo post añadido (respuesta):")
    print(json.dumps(response.json(), indent=4))
    print()

def actualizar_post(post_id, nuevo_titulo):
    """Actualiza el título de un post específico."""
    url = f"{URL}/posts/{post_id}"
    data = {
        "title": nuevo_titulo
    }
    response = requests.patch(url, json=data)
    print(f"Post {post_id} actualizado (respuesta):")
    print(json.dumps(response.json(), indent=4))
    print()

if __name__ == "__main__":
    obtener_posts_usuario(1)
    agregar_post("Mi nuevo Trabajo!", "Carlos Ashax paso por aqui!", 1)
    actualizar_post(1, "Consiguiendo un nuevo trabajo!")
