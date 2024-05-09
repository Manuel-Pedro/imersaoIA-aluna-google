"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": [genai.upload_file("<path>/image0.png")]
  },
  {
    "role": "user",
    "parts": [genai.upload_file("<path>/image1.png")]
  },
  {
    "role": "user",
    "parts": [genai.upload_file("<path>/image2.png")]
  },
  {
    "role": "user",
    "parts": ["Faça uma analise destas imagens, e diz se existe partes semelhantes nas imagens."]
  },
  {
    "role": "model",
    "parts": ["## Análise das Imagens:\n\nAs três imagens, apesar de distintas em termos de conteúdo, compartilham um elemento comum: **a representação da realidade humana**. Cada imagem captura um aspecto diferente da experiência humana:\n\n* **Imagem 1:** Retrata a realidade de um jovem em um ambiente empobrecido, provavelmente um país em desenvolvimento. A máscara sugere preocupações com saúde e higiene, talvez em um contexto de pandemia. A imagem transmite uma sensação de luta e resiliência diante da adversidade.\n* **Imagem 2:** Apresenta uma mulher em um campo de papoulas sob um céu dramático. A imagem evoca liberdade, beleza e conexão com a natureza. Ela contrasta fortemente com a primeira imagem, destacando a diversidade de experiências humanas.\n* **Imagem 3:** Mostra uma mulher utilizando um aplicativo de arte em seu celular. A imagem representa a interação humana com a tecnologia e a criatividade. Ela sugere um interesse em arte e design, possivelmente como forma de expressão pessoal.\n\n## Semelhanças entre as imagens:\n\nApesar das diferenças de contexto, as imagens apresentam as seguintes semelhanças:\n\n* **Protagonismo humano:** Todas as imagens têm pessoas como elemento central, enfatizando a experiência humana como tema principal.\n* **Expressão individual:** Cada imagem captura uma forma de expressão individual, seja através da luta pela sobrevivência, da apreciação da beleza natural ou da exploração da criatividade.\n* **Cores vibrantes:** As três imagens utilizam cores vibrantes, que contribuem para a transmissão de emoções e a criação de impacto visual.\n\n## Conclusão:\n\nAs imagens, embora distintas em conteúdo, convergem na representação da realidade humana em suas múltiplas facetas. Elas destacam a diversidade de experiências, emoções e formas de expressão que caracterizam a condição humana."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
