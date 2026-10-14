from collections.abc import Iterable, Sequence
from typing import Literal

type Alignment = Literal["left", "center", "right"]

_VALID_ALIGNMENTS = ("left", "center", "right")


class TextTable:
    """Gera tabelas de texto com largura dinâmica por coluna."""

    def __init__(
        self,
        headers: Sequence[object],
        rows: Iterable[Sequence[object]] = (),
        *,
        alignments: Sequence[Alignment] | None = None,
        row_separators: bool = False,
    ) -> None:
        """Inicializa uma tabela com cabeçalhos e linhas opcionais."""

        if isinstance(headers, (str, bytes)):
            raise TypeError(
                "headers deve ser uma sequência de cabeçalhos."
            )

        self._headers = tuple(str(header) for header in headers)

        if not self._headers:
            raise ValueError(
                "A tabela precisa ter pelo menos um cabeçalho."
            )

        if alignments is None:
            self._alignments = ("left",) * len(self._headers)
        else:
            if isinstance(alignments, (str, bytes)):
                raise TypeError(
                    "alignments deve conter um alinhamento por coluna."
                )

            if len(alignments) != len(self._headers):
                raise ValueError(
                    "A quantidade de alinhamentos deve ser "
                    "igual à quantidade de colunas."
                )

            invalid = [
                alignment
                for alignment in alignments
                if alignment not in _VALID_ALIGNMENTS
            ]

            if invalid:
                raise ValueError(
                    f"Alinhamentos inválidos: {invalid!r}. "
                    f"Use {_VALID_ALIGNMENTS}."
                )

            self._alignments = tuple(alignments)

        if not isinstance(row_separators, bool):
            raise TypeError("row_separators deve ser bool.")

        self._row_separators = row_separators
        self._rows: list[tuple[str, ...]] = []

        for row in rows:
            self.add_row(row)

    def add_row(self, values: Sequence[object]) -> None:
        """Adiciona uma linha, validando a quantidade de valores."""

        if isinstance(values, (str, bytes)):
            raise TypeError(
                "A linha deve ser uma sequência de valores."
            )

        row = tuple(str(value) for value in values)

        if len(row) != len(self._headers):
            raise ValueError(
                f"Esperadas {len(self._headers)} colunas; "
                f"recebidas {len(row)}."
            )

        self._rows.append(row)

    def _column_widths(self) -> list[int]:
        """Calcula a largura necessária para cada coluna."""

        widths = [len(header) for header in self._headers]

        for row in self._rows:
            for index, value in enumerate(row):
                widths[index] = max(
                    widths[index],
                    len(value),
                )

        return widths

    @staticmethod
    def _make_separator(widths: Sequence[int]) -> str:
        """Cria a linha que divide as colunas."""

        return "+" + "+".join(
            "-" * (width + 2)
            for width in widths
        ) + "+"

    def _format_row(
        self,
        values: Sequence[str],
        widths: Sequence[int],
    ) -> str:
        """Formata uma linha com o alinhamento configurado."""

        cells = []

        for value, width, alignment in zip(
            values,
            widths,
            self._alignments,
        ):
            if alignment == "left":
                formatted = value.ljust(width)
            elif alignment == "center":
                formatted = value.center(width)
            else:
                formatted = value.rjust(width)

            cells.append(f" {formatted} ")

        return "|" + "|".join(cells) + "|"

    def render(self) -> str:
        """Retorna a tabela formatada como uma string."""

        widths = self._column_widths()
        separator = self._make_separator(widths)

        lines = [
            separator,
            self._format_row(self._headers, widths),
            separator,
        ]

        for index, row in enumerate(self._rows):
            lines.append(self._format_row(row, widths))

            is_last_row = index == len(self._rows) - 1

            if self._row_separators and not is_last_row:
                lines.append(separator)

        if self._rows:
            lines.append(separator)

        return "\n".join(lines)

    def __str__(self) -> str:
        """Permite usar print(table)."""

        return self.render()
