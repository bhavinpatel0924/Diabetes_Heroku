mkdir -p ~/.streamlit/
echo "[general]
email = \"bhavipatel0924@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml