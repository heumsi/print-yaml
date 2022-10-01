from typing import Optional, Any, Iterable

import typer
import yaml


def create_dict_with_depth(
    source: Iterable | Any,
    current_depth: int,
    destination_depth: int,
    include_value: bool,
) -> dict | list | Any:
    if include_value and not isinstance(source, Iterable):
        return source
    if current_depth > destination_depth:
        return None

    if isinstance(source, dict):
        output = {}
        for k, v in source.items():
            output[k] = create_dict_with_depth(
                v, current_depth + 1, destination_depth, include_value
            )
    elif isinstance(source, list):
        output = []
        for item in source:
            output.append(
                create_dict_with_depth(
                    item, current_depth, destination_depth, include_value
                )
            )
    else:
        output = source
    return output


def format_result(result: str) -> str:
    result = result.replace("null", "")
    return result


def main(
    file_path: str,
    depth: Optional[int] = typer.Option(0, "-d", min=0),
    include_value: Optional[bool] = typer.Option(False, "--value", "-v"),
) -> None:
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
        if depth:
            output = create_dict_with_depth(data, 1, depth, include_value)
            result = yaml.dump(output, default_flow_style=False)
        else:
            result = yaml.dump(data, default_flow_style=False)
        result = format_result(result)
        print(result)


def run():
    typer.run(main)


if __name__ == "__main__":
    run()
