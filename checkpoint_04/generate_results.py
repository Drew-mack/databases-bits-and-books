"""Generate query_results.md and data.sql from the checked database."""
import re, sqlite3
from pathlib import Path
p=Path(__file__).resolve().parent
c=sqlite3.connect(f'file:{p / "database.sqlite"}?mode=ro',uri=True)
parts=re.split(r'-- \(([a-n])\) ([^\n]+)\n', (p/'queries.sql').read_text())
out=['# Checkpoint 04 query results', '', 'Generated from database.sqlite and queries.sql. Sample email for (b) and (e): avery.reader@example.com.', '']
for letter,title,sql in zip(parts[1::3],parts[2::3],parts[3::3]):
    cur=c.execute(sql.strip()); rows=cur.fetchall(); headers=[d[0] for d in cur.description]
    def cell(v): return str('' if v is None else v).replace('|','\\|').replace('\n',' ')
    out += [f'## ({letter}) {title}', '', '| ' + ' | '.join(map(cell,headers)) + ' |', '| ' + ' | '.join(['---']*len(headers)) + ' |']
    out += ['| ' + ' | '.join(map(cell,row)) + ' |' for row in rows]
    if not rows: out += ['','No matching rows.']
    out += ['',f'{len(rows)} row(s).','']
(p/'query_results.md').write_text('\n'.join(out))
insert=[line for line in c.iterdump() if line.startswith('INSERT INTO ') and not line.startswith('INSERT INTO "sqlite_sequence"')]
(p/'data.sql').write_text('-- Data exported from database.sqlite; run after schema.sql in a new SQLite database.\n-- Catalog comes from source_catalog.csv; sales and stock are demonstration data.\nPRAGMA foreign_keys = ON;\nBEGIN TRANSACTION;\nPRAGMA defer_foreign_keys = ON;\n'+'\n'.join(insert)+'\nCOMMIT;\n')
