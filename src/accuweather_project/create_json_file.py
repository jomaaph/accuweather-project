from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from accuweather_project.request import connect_to_accuweather


def create_json_file(data: Any, filename: str | Path) -> Path:
    """Save data as formatted UTF-8 JSON and return its path."""
    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Consulta localidades no AccuWeather.")
    parser.add_argument("location", help="Nome da cidade ou localidade")
    parser.add_argument("--country-code", default="AO", help="Codigo ISO do pais")
    parser.add_argument(
        "--output",
        default="data/accuweather_data.json",
        help="Caminho do arquivo JSON de saida",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    data = connect_to_accuweather(args.country_code, args.location)
    output_path = create_json_file(data, args.output)
    print(f"Dados salvos em {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())