BASE_STYLES = """
.jp-root {
    min-height: 100vh;
    box-sizing: border-box;
    padding: var(--jp-space-xl);
    font-family: var(--jp-font-family);
    color: var(--jp-text);
    background: var(--jp-bg);
}

/* ==========================================
   Layout Primitives
   ========================================== */

.jp-stack {
    display: flex;
    flex-direction: column;
    gap: var(--jp-space-lg);
}

.jp-row {
    display: flex;
    flex-direction: row;
    gap: var(--jp-space-md);
}

.jp-grid {
    display: grid;
    gap: var(--jp-space-lg);
}

.jp-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.jp-scroll-x {
    overflow-x: auto;
}

.jp-document-header {
    max-width: 960px;
    margin: 0 auto var(--jp-space-xl);
    padding-bottom: var(--jp-space-lg);
    border-bottom: 1px solid var(--jp-border);
}

.jp-document-title {
    margin: 0;
    font-size: clamp(2rem, 5vw, 3rem);
    line-height: 1.05;
    letter-spacing: -0.04em;
    color: var(--jp-title);
}

.jp-document-subtitle {
    margin: var(--jp-space-sm) 0 0;
    font-size: 1rem;
    font-weight: 700;
    color: var(--jp-key);
}

.jp-document-description {
    margin: var(--jp-space-md) 0 0;
    max-width: 720px;
    font-size: 1rem;
    line-height: 1.7;
    color: var(--jp-text);
}

.jp-content {
    max-width: 960px;
    margin: 0 auto;
}

.jp-card {
    border: 1px solid var(--jp-border);
    border-radius: var(--jp-radius);
    background: var(--jp-surface);
    box-shadow: var(--jp-shadow);
    overflow: hidden;
}

.jp-card-title {
    margin: 0;
    padding: var(--jp-space-lg);
    font-size: 1.35rem;
    line-height: 1.2;
    letter-spacing: -0.02em;
    color: var(--jp-title);
    border-bottom: 1px solid var(--jp-border);
    background: var(--jp-surface-soft);
}

.jp-card-fields {
    display: grid;
}

.jp-card-field {
    display: grid;
    grid-template-columns: minmax(140px, 220px) 1fr;
    gap: var(--jp-space-md);
    align-items: start;
    padding: var(--jp-space-md) var(--jp-space-lg);
    border-bottom: 1px solid var(--jp-border);
}

.jp-card-field:last-child {
    border-bottom: none;
}

.jp-card-key {
    font-size: 0.9rem;
    font-weight: 800;
    letter-spacing: 0.01em;
    color: var(--jp-key);
}

.jp-card-value {
    line-height: 1.6;
    color: var(--jp-value);
    overflow-wrap: anywhere;
}

.jp-value-muted {
    color: var(--jp-muted);
    font-style: italic;
}

.jp-value-boolean {
    font-weight: 700;
    color: var(--jp-key);
}

.jp-value-link {
    color: var(--jp-key);
    font-weight: 700;
    text-decoration: none;
    border-bottom: 1px solid currentColor;
}

.jp-value-link:hover {
    opacity: 0.8;
}

.jp-value-date {
    font-weight: 600;
    color: var(--jp-value);
}

.jp-table {
    width: 100%;
    border-collapse: collapse;
    border: 1px solid var(--jp-border);
    border-radius: var(--jp-radius);
    background: var(--jp-surface);
    box-shadow: var(--jp-shadow);
    overflow: hidden;
}

.jp-table th,
.jp-table td {
    padding: var(--jp-space-md);
    border-bottom: 1px solid var(--jp-border);
    text-align: left;
}

.jp-table th {
    color: var(--jp-title);
    background: var(--jp-surface-soft);
}

.jp-table tr:last-child td {
    border-bottom: none;
}

.jp-tree {
    margin: var(--jp-space-sm) 0 0 var(--jp-space-lg);
    padding-left: var(--jp-space-md);
    border-left: 1px solid var(--jp-border);
}

.jp-tree li {
    margin: var(--jp-space-sm) 0;
}

.jp-tree-label {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: calc(var(--jp-radius) / 2);
    background: var(--jp-surface-soft);
    color: var(--jp-text);
}

.jp-card-field-nested,
.jp-card-field-collection {
    align-items: start;
}

.jp-disclosure {
    width: 100%;
}

.jp-disclosure-summary {
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: var(--jp-space-sm);
    padding: 0.4rem 0.75rem;
    border: 1px solid var(--jp-border);
    border-radius: calc(var(--jp-radius) / 2);
    background: var(--jp-surface-soft);
    color: var(--jp-key);
    font-weight: 700;
    list-style: none;
    transition:
        background 0.2s ease,
        transform 0.2s ease;
}

.jp-disclosure-summary:hover {
    background: var(--jp-surface);
    transform: translateY(-1px);
}

.jp-disclosure-summary::-webkit-details-marker {
    display: none;
}

.jp-disclosure-summary::before {
    content: "▸";
    display: inline-block;
    transition: transform 0.2s ease;
}

.jp-disclosure[open] .jp-disclosure-summary::before {
    transform: rotate(90deg);
}

.jp-disclosure-content {
    margin-top: var(--jp-space-md);
    padding-left: var(--jp-space-md);
    border-left: 2px solid var(--jp-border);
}

.jp-disclosure-content .jp-card {
    box-shadow: none;
    border-style: dashed;
}

.jp-collection-item {
    padding: 0.65rem 0.85rem;
    border: 1px solid var(--jp-border);
    border-radius: calc(var(--jp-radius) / 2);
    background: var(--jp-surface-soft);
}

@media (max-width: 640px) {
    .jp-root {
        padding: var(--jp-space-lg);
    }

    .jp-card-field {
        grid-template-columns: 1fr;
        gap: var(--jp-space-sm);
    }

    .jp-document-title {
        font-size: 2rem;
    }
}
"""
