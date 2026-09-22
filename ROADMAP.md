# Roadmap do AccuWeather Project

## Objetivo

Construir uma pequena aplicação Python capaz de consultar dados meteorológicos do AccuWeather, persistir os resultados e preparar os dados para análise com pandas.

## Estado atual

- [x] Projeto configurado com `uv`.
- [x] Dependências principais instaladas: `requests`, `python-dotenv`, `pandas` e `ipykernel`.
- [x] Chave da API carregada por variável de ambiente.
- [x] Consulta de localização implementada.
- [x] Resultado salvo em JSON.
- [x] Projeto publicado no GitHub.
- [x] Testes automatizados.
- [x] Documentação de instalação e uso.
- [ ] Consulta de previsão meteorológica.

## Fase 1: Estabilização

- [x] Escolher um único módulo de requisições e remover duplicidade entre `request.py` e `accuweather_request.py`.
- [x] Remover chamadas executadas automaticamente durante importação.
- [x] Corrigir a assinatura e o retorno da função de consulta.
- [x] Corrigir o uso de autenticação: enviar a chave apenas como parâmetro `apikey`.
- [x] Renomear `create_json_flile.py` para `create_json_file.py`.
- [x] Validar a variável obrigatória `API_KEY` com mensagem clara e usar URL configurável.
- [x] Ignorar arquivos JSON gerados no repositório.

## Fase 2: Qualidade e testes

- [x] Criar testes unitários para a função de requisição.
- [x] Simular respostas da API sem depender da internet durante os testes.
- [x] Validar resposta inválida e criação do arquivo e diretório de saída.
- [ ] Adicionar lint e formatação ao projeto.
- [ ] Adicionar integração contínua no GitHub Actions.

## Fase 3: Funcionalidades da API

- [ ] Criar função para buscar a chave da cidade por país e localização.
- [ ] Consultar condições meteorológicas atuais.
- [ ] Consultar previsão diária e horária.
- [x] Permitir configurar cidade, país e arquivo de saída por argumentos de linha de comando.
- [ ] Implementar cache local para reduzir chamadas repetidas à API.
- [ ] Tratar limite de requisições e respostas `429`.

## Fase 4: Dados e análise

- [ ] Normalizar a resposta da API em um modelo de dados consistente.
- [ ] Exportar dados também para CSV.
- [ ] Usar pandas para criar uma tabela histórica.
- [ ] Registrar data e hora da coleta.
- [ ] Criar notebook documentando a exploração dos dados.
- [ ] Produzir gráficos básicos de temperatura e condições meteorológicas.

## Fase 5: Entrega

- [x] Completar o `README.md` com instalação, configuração e exemplos.
- [x] Adicionar um arquivo `.env.example` sem credenciais reais.
- [ ] Documentar os endpoints utilizados.
- [ ] Criar uma interface de linha de comando estável.
- [ ] Criar uma release `v0.1.0` após os testes passarem.

## Próximo marco

O MVP está concluído: existe um comando único, documentado e testado para consultar uma localização e salvar o resultado em JSON. O próximo incremento é consultar condições atuais e previsões meteorológicas.
