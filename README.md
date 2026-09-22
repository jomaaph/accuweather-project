# AccuWeather Project

Aplicacao Python para consultar localidades no AccuWeather e salvar os resultados em JSON.

## Requisitos

- Python 3.12 ou superior
- `uv`
- Uma chave de API do AccuWeather

## Instalacao

```bash
uv sync
```

Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Depois, preencha `API_KEY` com sua chave. A variavel `URL` pode ser alterada para outro endpoint de localidades.

## Uso

Consultar Luanda, Angola e salvar em `data/accuweather_data.json`:

```bash
uv run accuweather-project Luanda --country-code AO
```

Escolher outro arquivo de saida:

```bash
uv run accuweather-project Luanda --country-code AO --output data/luanda.json
```

Também é possível executar diretamente:

```bash
uv run python -m accuweather_project.create_json_file Luanda --country-code AO
```

## Testes

```bash
uv run pytest
```

Os testes simulam a API e não exigem conexão com a internet.

## Estrutura

- `src/accuweather_project/request.py`: cliente da API.
- `src/accuweather_project/create_json_file.py`: CLI e persistência JSON.
- `tests/`: testes automatizados.
- `ROADMAP.md`: histórico e próximos passos do projeto.
