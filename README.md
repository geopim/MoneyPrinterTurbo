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

## Como Rodar via Terminal (Windows) 🚀

Se você deseja rodar o sistema diretamente pelo terminal (Powershell ou CMD), siga estes passos:

1. **Ative o ambiente virtual**:
   ```powershell
   .\.venv\Scripts\activate
   ```
2. **Execute o Backend**:
   ```powershell
   python main.py
   ```
3. **Execute a Interface Web (WebUI)**:
   Em uma **nova janela** de terminal (com o ambiente ativado):
   ```powershell
   streamlit run .\webui\Main.py
   ```

Ou simplesmente execute o arquivo `webui.bat` na raiz do projeto.

## Usando Vídeos do Pixabay 🎥

Para usar o Pixabay como fonte de seus vídeos, siga estas etapas:

1. **Obtenha uma chave de API**: Crie uma conta no [Pixabay](https://pixabay.com/api/docs/) e copie sua chave de API.
2. **Configure o `config.toml`**: Abra o arquivo `config.toml` na raiz do projeto e localize as seguintes linhas:
   ```toml
   [app]
   video_source = "pixabay"  # Mude de "pexels" para "pixabay"
   pixabay_api_keys = [ "SUA_CHAVE_AQUI" ]
   ```
3. **Reinicie o sistema**: Após salvar as alterações, os vídeos serão buscados no Pixabay.

## Requisitos do Sistema 📦

- Recomendado mínimo 4 núcleos de CPU, 4G de RAM. GPU não é obrigatória.
- Windows 10 ou MacOS 11.0 e versões posteriores.

## Instalação e Implantação 📥

### Pré-requisitos

#### ① Clonar o Projeto
```shell
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```

#### ② Modificar o Arquivo de Configuração
- Copie o arquivo `config.example.toml` e renomeie para `config.toml`.
- Configure as chaves de API e o provedor LLM (como Gemini ou OpenAI).

### Implantação com Docker 🐳

```shell
cd MoneyPrinterTurbo
docker-compose up
```
Acesse a Web Interface em http://localhost:8501.

---

## Feedback & Sugestões 📢

- Você pode enviar um [issue](https://github.com/harry0703/MoneyPrinterTurbo/issues) ou um [pull request](https://github.com/harry0703/MoneyPrinterTurbo/pulls).

## Licença 📝

Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.