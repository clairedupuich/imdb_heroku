#配置cd
mkdir -p ~/.streamlit/




echo "\

[server]\n\

headless = true\n\

port = $PORT\n\

ennbleCORS = false\n\

\n\

" > ~/.streamlit/config.toml