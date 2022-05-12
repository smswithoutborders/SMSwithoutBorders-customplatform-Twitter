import tweepy
import json

token_path = 'test/token.json'
credentials_path = 'test/credentials.json'

c = open(credentials_path)
credentials = json.load(c)

print(f"\nDeveloper credentials: {credentials}\n")

def main():
    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id=credentials["client_id"],
        redirect_uri=credentials["redirect_uri"],
        scope=["tweet.write", "users.read", "tweet.read", "offline.access"],
        client_secret=credentials["client_secret"]
    )

    authorize_url = oauth2_user_handler.get_authorization_url()
    print(f"Click the authorize url: \n{authorize_url}\n")

    resp = input("Paste Response URI here: ")

    access_token = oauth2_user_handler.fetch_token(resp)

    print(f"\nToken: {access_token}\n")
    with open(token_path, 'w') as t:
        json.dump(access_token, t, ensure_ascii=False, indent=4)

    print(f"token successfully stored in {token_path}")

if __name__ == "__main__":
    main()