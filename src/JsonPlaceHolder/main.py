import requests

if __name__ == "__main__":

    request = requests.get("https://jsonplaceholder.typicode.com/users")
    print("========= Première Partie ========= Requête Get")
    if request.status_code != 200:
        print("Erreur :" + request.status_code)
    else:
        for item in request.json():
            print(f"{item['name']} - {item['email']}")
        print("\n")

    request = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
    print("========= Seconde Partie ========= Requête Get avec filtre")
    if request.status_code != 200:
        print("Erreur :" + str(request.status_code))
    else:
        for item in request.json():
            print(item["title"])
        print("\n")

    post = {
        "title": "Mon nouveau post",
        "body": "Ceci est le contenu de mon post",
        "userId": 1
    }
    request = requests.post("https://jsonplaceholder.typicode.com/posts", json=post)
    print("========= Troisième Partie ========= Requête Post")
    if request.status_code != 201:
        print("Erreur :" + str(request.status_code))
    else:
        for key, value in request.json().items():
            print(f"{key} : {value}")
    print("\n")


    def get_user_posts(user_id):
        answer = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": user_id})

        if answer.status_code != 200:
            raise Exception(f"Erreur HTTP {answer.status_code}")

        posts = answer.json()
        if not posts:
            return "Rien !"
        return [post["title"] for post in posts]

    print("========= Qatrième Partie ========= Requête via fonction et gestion erreur")
    for title in get_user_posts(1):
        print(title)