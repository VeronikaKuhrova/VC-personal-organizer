# Personal Organizer – nastavení kódovacího agenta Codex

Hlavním cílem projektu není samotný správce úkolů, ale demonstrace nastavení a použití kódovacího agenta s využitím:

* Codex
* `AGENTS.md`
* vlastního Skillu
* vlastního Subagenta
* vlastního MCP serveru

V projektu nejsou použity žádné pluginy ani Marketplace.

## Personal Organizer

Aplikace je jednoduchý správce úkolů pro příkazovou řádku napsaný v Pythonu.

Umožňuje:

* přidávat úkoly,
* zobrazovat seznam úkolů,
* označovat úkoly jako dokončené,
* přiřazovat prioritu `low`, `medium` nebo `high`,
* ukládat úkoly lokálně do souboru `tasks.json`.

Aplikaci lze spustit příkazem:

```bash
python3 main.py
```

## Instrukce pro kódovacího agenta

Projektové instrukce pro Codex jsou uloženy v souboru:

```text
AGENTS.md
```

Tento soubor definuje:

* cíl projektu,
* pravidla vývoje,
* požadovanou kompatibilitu s Pythonem,
* omezení používání externích závislostí,
* očekávanou agentní architekturu.

Funkčnost byla ověřena tak, že byl Codex požádán o shrnutí instrukcí, které při spuštění projektu načetl.

Codex následně při tvorbě aplikace respektoval instrukce uložené v `AGENTS.md`.

## Vlastní Skill

Vlastní Skill je uložen v:

```text
.agents/skills/task-organizer/SKILL.md
```

Skill definuje pravidla, podle kterých má agent vyhodnocovat priority úkolů.

Použitá pravidla například určují:

* `high` – urgentní termíny, důležitá odevzdání nebo úkoly blokující další práci,
* `medium` – důležité úkoly, které je potřeba splnit brzy, ale nejsou bezprostředně urgentní,
* `low` – rutinní, volitelné nebo neurgentní úkoly.

Skill byl otestován tím, že Codex dostal několik různých úkolů a měl jim podle pravidel Skillu doporučit prioritu.

## Subagent

Specializovaný Subagent `planner` je nakonfigurován pomocí souborů:

```text
.codex/config.toml
.codex/agents/planner.toml
```

Úlohou Subagenta je:

* posoudit seznam úkolů,
* zohlednit jejich prioritu a termíny,
* doporučit pořadí jejich řešení,
* stručně vysvětlit doporučení.

Subagent pracuje v režimu `read-only` a nemá měnit soubory projektu.

Funkčnost byla ověřena delegováním plánovacího úkolu z hlavního Codex agenta na Subagenta `planner`.

## Vlastní MCP server

Vlastní MCP server je implementován v:

```text
mcp/server.py
```

Server zpřístupňuje Codexu dva vlastní nástroje:

```text
list_tasks
add_task
```

Pomocí nich může Codex pracovat s úkoly v Personal Organizeru prostřednictvím Model Context Protocolu, aniž by musel přímo číst nebo ručně upravovat soubor `tasks.json`.

MCP server se spouští pomocí:

```text
mcp/run_server.sh
```

## Instalace prostředí pro MCP

MCP server vyžaduje Python 3.10 nebo novější.

V projektu byl použit Python 3.12.

Příklad vytvoření samostatného prostředí:

```bash
python3.12 -m venv .venv-mcp
.venv-mcp/bin/python -m pip install -r requirements-mcp.txt
```

Virtuální prostředí `.venv-mcp` není součástí Git repozitáře.

Codex následně spouští MCP server podle konfigurace uložené v:

```text
.codex/config.toml
```

## Ověření MCP serveru

MCP integrace byla prakticky otestována.

Codex pomocí vlastního MCP serveru:

1. zobrazil existující úkoly pomocí `list_tasks`,
2. přidal nový úkol pomocí `add_task`,
3. znovu zobrazil seznam úkolů a potvrdil, že nový úkol byl uložen.

Při testování Codex zobrazil MCP server:

```text
personal_organizer
```

se dvěma dostupnými nástroji.

## Struktura projektu

```text
personal-organizer/
├── .agents/
│   └── skills/
│       └── task-organizer/
│           └── SKILL.md
├── .codex/
│   ├── agents/
│   │   └── planner.toml
│   └── config.toml
├── mcp/
│   ├── server.py
│   └── run_server.sh
├── .gitignore
├── AGENTS.md
├── README.md
├── main.py
├── requirements-mcp.txt
└── tasks.json
```

## Splnění zadání

Projekt demonstruje:

* **Kódovací agent:** Codex
* **MCP Server:** vlastní Personal Organizer MCP server
* **Skill:** vlastní `task-organizer` Skill
* **Subagent:** vlastní `planner` Subagent


