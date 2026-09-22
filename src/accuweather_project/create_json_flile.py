import json
from pathlib import Path
from typing import Any

from accuweather_project.request import connect_to_accuweather


def create_json_file(data: Any, filename: str | Path) -> Path:
    """
    criar um arquivo JSON com os dados fornecidos e salvar no caminho especificado.
    Args:
        data (Any): Os dados a serem salvos no arquivo JSON.
        filename (str | Path): O caminho do arquivo JSON a ser criado.
    Returns:
        Path: O caminho do arquivo JSON criado.
    """

    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return output_path


def main() -> None:
    data = connect_to_accuweather("AO", "Luanda")
    output_path = create_json_file(data, Path("data") / "accuweather_data.json")
    print(f"Dados salvos em {output_path}")


if __name__ == "__main__":
    main()