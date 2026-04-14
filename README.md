<div align="center">
<h1 align="center">MoneyPrinterTurbo 💸</h1>

<p align="center">
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/stargazers"><img src="https://img.shields.io/github/stars/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues"><img src="https://img.shields.io/github/issues/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/network/members"><img src="https://img.shields.io/github/forks/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/harry0703/MoneyPrinterTurbo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/harry0703/MoneyPrinterTurbo.svg?style=for-the-badge" alt="License"></a>
</p>

<h3><a href="README-en.md">English</a> | <a href="README-zh.md">简体中文</a> | Português</h3>

<div align="center">
  <a href="https://trendshift.io/repositories/8731" target="_blank"><img src="https://trendshift.io/api/badge/repositories/8731" alt="harry0703%2FMoneyPrinterTurbo | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

Basta fornecer um **tópico** ou **palavra-chave** para um vídeo, e ele gerará automaticamente o roteiro, materiais de vídeo, legendas e música de fundo antes de sintetizar um vídeo curto em alta definição.

### WebUI

![](docs/webui-en.jpg)

### Interface API

![](docs/api.jpg)

</div>

## Agradecimentos Especiais 🙏

Devido ao processo de **implantação** e **uso** deste projeto, existe uma certa barreira para usuários iniciantes. Gostaríamos de expressar nossos agradecimentos especiais a:

**RecCloud (Plataforma de Serviço Multimídia com AI)** por fornecer um serviço gratuito de `Gerador de Vídeo com IA` baseado neste projeto. Ele permite o uso online sem necessidade de implantação.

- Versão Chinesa: https://reccloud.cn
- Versão Inglesa: https://reccloud.com

![](docs/reccloud.com.jpg)

## Funcionalidades 🎯

- [x] Arquitetura **MVC completa**, código **claro e estruturado**, fácil de manter, suporte para `API` e `Interface Web`
- [x] Suporte para roteiro gerado por **IA** ou **customizado**
- [x] Suporte a vários tamanhos de **vídeo HD**
    - [x] Retrato 9:16, `1080x1920`
    - [x] Paisagem 16:9, `1920x1080`
- [x] Suporte para **geração de vídeos em lote**
- [x] Suporte para configurar a **duração dos clipes**
- [x] Suporte para roteiros em **Português**, **Inglês** e **Chinês**
- [x] Suporte a **múltiplas vozes** com **pré-visualização em tempo real**
- [x] Suporte para **geração de legendas** personalizáveis (fonte, posição, cor, tamanho, contorno)
- [x] Suporte para **música de fundo** (aleatória ou específica)
- [x] Materiais de vídeo em **alta definição** e **livres de direitos autorais**, além de suporte a **materiais locais**
- [x] Integração com: **OpenAI**, **Moonshot**, **Azure**, **gpt4free**, **one-api**, **Qwen**, **Google Gemini**, **Ollama**, **DeepSeek**, **Pollinations**, **ModelScope** e mais

## Requisitos de Sistema 📦

- **Sistema**: Windows 10, MacOS 11.0+ ou distribuições Linux populares.
- **GPU**: Não obrigatória, mas recomendada para transcrição local (`faster-whisper`) e processamento mais rápido.

| Item | Mínimo | Recomendado | Ideal |
| --- | --- | --- | --- |
| CPU | 4 Cores | 6 a 8 Cores | 8+ Cores |
| RAM | 4 GB | 8 GB | 16 GB+ |
| GPU | N/A | 4 GB VRAM+ | 8 GB VRAM+ |

## Como Rodar via Terminal (Windows) 🚀

Para rodar o sistema diretamente pelo terminal (Powershell ou CMD), escolha uma das formas abaixo:

### 1. Recomendado: Usando `uv` (Mais rápido e estável)
Se você instalou o [uv](https://docs.astral.sh/uv/):
```powershell
uv run python main.py  # Iniciar Backend
uv run streamlit run ./webui/Main.py # Iniciar WebUI
```

### 2. Manual (Venv + Pip)
```powershell
.\.venv\Scripts\activate
python main.py  # Iniciar Backend
streamlit run .\webui\Main.py # Iniciar WebUI
```

Ou simplesmente execute o arquivo `webui.bat` na raiz do projeto.

## Usando Vídeos do Pixabay 🎥

Para usar o Pixabay como fonte de seus vídeos:

1. **API Key**: Obtenha sua chave em [Pixabay API](https://pixabay.com/api/docs/).
2. **Setup**: No arquivo `config.toml`, mude `video_source = "pixabay"` e adicione sua chave em `pixabay_api_keys = [ "SUA_CHAVE_AQUI" ]`.
3. **Reinicie**: Salve e reinicie o backend e a interface.

## Instalação e Implantação 📥

### Docker 🐳
```shell
cd MoneyPrinterTurbo
docker-compose up
```
Acesse em http://localhost:8501.

### Instalação Manual com `uv`
```shell
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
uv python install 3.11
uv sync --frozen
```

---

## Feedback & Sugestões 📢

- Envie um [issue](https://github.com/harry0703/MoneyPrinterTurbo/issues) ou um [pull request](https://github.com/harry0703/MoneyPrinterTurbo/pulls).

## Licença 📝

Veja o arquivo [`LICENSE`](LICENSE).
