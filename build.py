import sys, re
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf8").read()
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
i = s.index("</style>") + len("</style>")
head, body = s[:i], s[i:]
doc = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  '<meta name="description" content="Séances guidées de renforcement profond du dos, mobilité, tendons et fascias, avec suivi.">\n'
  '<meta name="theme-color" content="#0E6873">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'
  '<meta name="apple-mobile-web-app-title" content="Colonne Active">\n'
  '<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icon.svg" type="image/svg+xml">\n'
  '<link rel="apple-touch-icon" href="icon-192.png">\n'
  '<style>[hidden]{display:none!important}body{margin:0}</style>\n'
  + head + '\n</head>\n<body>' + body + '\n</body>\n</html>\n')
open(out, "w", encoding="utf8").write(doc)
