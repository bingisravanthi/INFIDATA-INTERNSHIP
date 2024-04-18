from streamlit_authenticator.utilities.hasher import Hasher
import streamlit_authenticator as stauth

hashed_passwords = Hasher(['sravs']).generate()
print(hashed_passwords)
