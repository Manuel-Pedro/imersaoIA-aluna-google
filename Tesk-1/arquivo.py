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

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file.uri]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1].uri]

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "user",
    "parts": ["\n\nPor meio desse conjunto de dados faça uma analise profunda de todos os dados, e extrai conclusões de como eu tenho utilizado o meu tempo, criando um resumo do que eu mais acesso, quantidade de uso e tipo de site."]
  },
  {
    "role": "model",
    "parts": ["## Análise do histórico de navegação:\n\nPara analisar seu histórico de navegação e entender como você tem utilizado seu tempo, vamos segmentar a informação por categorias e destacar os pontos mais relevantes:\n\n**1. Ferramentas de Desenvolvimento e Ciência de Dados:**\n\n* **Domínio:** Grande parte do seu histórico revela uso de ferramentas e plataformas relacionadas a desenvolvimento e ciência de dados.\n* **Exemplos:** Jupyter Notebook, Google AI Studio, Google Cloud Platform, Python, Pandas, NumPy, Scikit-learn,  WorldQuant University, Codecademy, Kaggle.\n* **Conclusão:** Você dedica um tempo significativo ao aprendizado e prática de programação e análise de dados. Isso indica um forte interesse e possível carreira nessa área.\n\n**2. Tradução e Linguagem:**\n\n* **Frequência:** Observamos um uso frequente do Google Tradutor, sugerindo a necessidade de lidar com conteúdo em diferentes idiomas. \n* **Conclusão:** Você pode estar aprendendo um novo idioma, traduzindo documentos ou trabalhando em projetos que envolvem múltiplas línguas. \n\n**3. Design e Interface:**\n\n* **Exploração:** Há registros de pesquisas e acesso a plataformas de design como Figma, Adobe XD e Qt Designer.\n* **Conclusão:** Você demonstra curiosidade e possivelmente está explorando o campo do design de interface e experiência do usuário (UI/UX).\n\n**4. Educação e Cursos Online:**\n\n* **Plataformas:** Identificamos acesso a plataformas de cursos online como Udemy, Codecademy e Data Science Academy.\n* **Conclusão:** Você investe em aprendizado contínuo e desenvolvimento de habilidades em diferentes áreas.\n\n**5. Redes Sociais e Entretenimento:**\n\n* **Presença moderada:**  Observamos visitas ao Instagram e YouTube, mas em menor frequência que as categorias anteriores.\n* **Conclusão:** Você utiliza redes sociais e plataformas de entretenimento, mas aparentemente com moderação.\n\n**6. Outras Categorias:**\n\n* **Exemplos:** Google Search, Gmail, MEGA, openAFRICA, VirtualBox, LaTeX. \n* **Conclusão:** O histórico demonstra uso de diversas ferramentas e plataformas para finalidades específicas.\n\n## Resumo:\n\nSua atividade online indica um foco principal em **programação, ciência de dados e desenvolvimento**. Você investe tempo em aprendizado e prática dessas áreas, sugerindo uma possível carreira ou projeto pessoal significativo. Adicionalmente, demonstra interesse em **design e interface**, além de buscar **educação e desenvolvimento de habilidades** por meio de cursos online. O uso de **redes sociais e entretenimento** parece moderado, indicando um equilíbrio em suas atividades online.\n\n**Recomendações:**\n\n* **Explore ferramentas de gestão de tempo:**  Aplicativos como RescueTime ou Toggl podem fornecer insights detalhados sobre seu uso do tempo no computador.\n* **Utilize extensões de foco:** Extensões como StayFocusd ou Forest podem ajudar a minimizar distrações e manter o foco em tarefas importantes. \n* **Crie um plano de estudo:**  Organize seu tempo dedicado a aprendizado e defina metas específicas para maximizar sua produtividade. \n\n\n**Observação:** Esta análise se baseia no conjunto de dados fornecido até novembro de 2023. Seu comportamento de navegação pode ter mudado desde então."]
  },
  {
    "role": "user",
    "parts": ["analisa mais os dados faltantes"]
  },
  {
    "role": "model",
    "parts": ["## Análise Adicional:\n\nVamos explorar outros aspectos relevantes do seu histórico de navegação:\n\n**1. Padrões de Horário:**\n\n* **Maior atividade:** A maioria das entradas se concentra entre as 10h e 22h, sugerindo que você é mais ativo online durante o dia e início da noite. \n* **Atividade noturna:** Há alguns registros de uso durante a madrugada, possivelmente relacionados a estudos, projetos pessoais ou simplesmente hábitos de navegação noturnos.\n\n**2. Tipos de Sites:**\n\n* **Predominância de sites educativos/profissionais:** A maior parte dos sites acessados está relacionada a educação, desenvolvimento e trabalho. Isso reforça seu foco em aprendizado e produtividade.\n* **Sites de entretenimento:** Há presença de sites de entretenimento, mas em menor quantidade, sugerindo um uso mais casual e menos frequente.\n\n**3. Sites com Múltiplas Visitas:**\n\n* **Exemplos:** Google Cloud Innovators, Google Developer Profile, ChatGPT, Instagram, JupyterLab, Conta do Google.\n* **Conclusão:** Esses sites podem representar seus principais interesses ou ferramentas de trabalho que você utiliza com frequência.\n\n**4. Sites de Busca:**\n\n* **Uso frequente do Google Search:** Isso demonstra a busca ativa por informação e soluções para problemas ou dúvidas. \n* **Pesquisas variadas:** As consultas de busca abrangem diversos temas, desde programação e ciência de dados até design e entretenimento, refletindo a amplitude de seus interesses. \n\n**5. Sites com Interações:**\n\n* **Exemplos:** Alura (form_submit), Google AI Studio (typed), Google Cloud Platform (link).\n* **Conclusão:** Esses registros indicam uma participação ativa em cursos, projetos e plataformas online, além da simples navegação.\n\n## Conclusões Adicionais:\n\n* **Equilíbrio:** Você parece equilibrar o tempo dedicado a atividades produtivas com momentos de lazer e entretenimento.\n* **Curiosidade:** A variedade de sites e pesquisas sugere uma mente curiosa e aberta a novos conhecimentos. \n* **Aprendizagem Contínua:** O acesso frequente a plataformas de cursos online e sites educativos indica um compromisso com a aprendizagem contínua.\n\n**Sugestões:**\n\n* **Analise as pesquisas do Google Search:** Elas podem revelar insights valiosos sobre seus interesses, desafios e áreas de foco.\n* **Explore os sites com múltiplas visitas:** Identifique os motivos dessas visitas recorrentes e avalie como esses sites contribuem para seus objetivos.\n* **Observe os padrões de horário:**  Analise se sua atividade online se alinha com seus níveis de energia e produtividade ao longo do dia.\n\n**Lembre-se:** \nEsta análise é limitada pelos dados fornecidos e não captura a totalidade de sua atividade online. Use-a como um ponto de partida para refletir sobre seus hábitos e como você pode otimizar seu tempo online para atingir seus objetivos."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)
