from html import escape

from json_presenter.formatting.values import format_value
from json_presenter.presentation import (
    CardNode,
    CollectionField,
    NestedField,
    PresentationDocument,
    PresentationNode,
    PrimitiveField,
    TableNode,
    TreeNode,
)


class HtmlRenderer:
    """Render a PresentationDocument into an HTML fragment."""

    def render(self, document: PresentationDocument) -> str:
        header_html = self._render_document_header(document)
        nodes_html = "\n".join(self._render_node(node)
                               for node in document.nodes)

        return f"""
        {header_html}
        <section class="jp-content jp-stack">
            {nodes_html}
        </section>
        """

    def _render_document_header(self, document: PresentationDocument) -> str:
        subtitle_html = (
            f'<p class="jp-document-subtitle">{escape(document.subtitle)}</p>'
            if document.subtitle
            else ""
        )

        description_html = (
            f'<p class="jp-document-description">{escape(document.description)}</p>'
            if document.description
            else ""
        )

        return f"""
        <header class="jp-document-header">
            <h1 class="jp-document-title">{escape(document.title)}</h1>
            {subtitle_html}
            {description_html}
        </header>
        """

    def _render_node(self, node: PresentationNode) -> str:
        if isinstance(node, CardNode):
            return self._render_card(node)

        if isinstance(node, TableNode):
            return self._render_table(node)

        if isinstance(node, TreeNode):
            return self._render_tree(node)

        raise TypeError(
            f"Unsupported presentation node: {type(node).__name__}")

    def _render_card(self, node: CardNode) -> str:
        fields_html = "\n".join(self._render_card_field(field)
                                for field in node.fields)

        return f"""
        <section class="jp-card">
            <h2 class="jp-card-title">{escape(node.title)}</h2>
            <div class="jp-card-fields">
                {fields_html}
            </div>
        </section>
        """

    def _render_card_field(
        self,
        field: PrimitiveField | NestedField | CollectionField,
    ) -> str:
        if isinstance(field, PrimitiveField):
            return self._render_primitive_field(field)

        if isinstance(field, NestedField):
            return self._render_nested_field(field)

        if isinstance(field, CollectionField):
            return self._render_collection_field(field)

        raise TypeError(f"Unsupported card field: {type(field).__name__}")

    def _render_primitive_field(self, field: PrimitiveField) -> str:
        return f"""
        <div class="jp-card-field">
            <span class="jp-card-key">{escape(field.label)}</span>
            <span class="jp-card-value">{format_value(field.content).html}</span>
        </div>
        """

    def _render_nested_field(self, field: NestedField) -> str:
        nested_card_html = self._render_card(field.card)
        field_count = len(field.card.fields)

        return f"""
        <div class="jp-card-field jp-card-field-nested">
            <span class="jp-card-key">{escape(field.label)}</span>
            <details class="jp-disclosure">
                <summary class="jp-disclosure-summary">
                    {escape(field.label)} · {field_count} field{'s' if field_count != 1 else ''}
                </summary>
                <div class="jp-disclosure-content">
                    {nested_card_html}
                </div>
            </details>
        </div>
        """

    def _render_collection_field(self, field: CollectionField) -> str:
        items_html = "\n".join(self._render_collection_item(item)
                               for item in field.items)
        item_count = len(field.items)
        item_label = self._get_collection_item_label(field)

        return f"""
        <div class="jp-card-field jp-card-field-collection">
            <span class="jp-card-key">{escape(field.label)}</span>
            <details class="jp-disclosure">
                <summary class="jp-disclosure-summary">
                    {escape(field.label)} · {item_count} {item_label}
                </summary>
                <div class="jp-disclosure-content jp-stack">
                    {items_html}
                </div>
            </details>
        </div>
        """

    def _get_collection_item_label(self, field: CollectionField) -> str:
        count = len(field.items)

        if count == 1:
            return "item"

        if all(isinstance(item, CardNode) for item in field.items):
            return "cards"

        return "items"

    def _render_collection_item(self, item: PrimitiveField | CardNode) -> str:
        if isinstance(item, PrimitiveField):
            return f"""
            <div class="jp-collection-item">
                <span class="jp-card-value">{format_value(item.content).html}</span>
            </div>
            """

        if isinstance(item, CardNode):
            return self._render_card(item)

        raise TypeError(f"Unsupported collection item: {type(item).__name__}")

    def _render_table(self, node: TableNode) -> str:
        headers_html = "\n".join(
            f"<th>{escape(str(header))}</th>" for header in node.headers
        )

        rows_html = "\n".join(
            self._render_table_row(row, node.headers) for row in node.rows
        )

        return f"""
        <div class="jp-scroll-x">
            <table class="jp-table">
                <thead>
                    <tr>
                        {headers_html}
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        """

    def _render_table_row(self, row: dict, headers: list[str]) -> str:
        cells_html = "\n".join(
            f"<td>{escape(str(row.get(header, '')))}</td>" for header in headers
        )

        return f"""
        <tr>
            {cells_html}
        </tr>
        """

    def _render_tree(self, node: TreeNode) -> str:
        children_html = "\n".join(self._render_tree(child)
                                  for child in node.children)

        if children_html:
            return f"""
            <li>
                <span class="jp-tree-label">{escape(node.label)}</span>
                <ul class="jp-tree">
                    {children_html}
                </ul>
            </li>
            """

        return f"""
        <li>
            <span class="jp-tree-label">{escape(node.label)}</span>
        </li>
        """
