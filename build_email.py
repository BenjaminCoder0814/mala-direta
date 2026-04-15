import urllib.parse

BASE = "https://zenith-lacres-catalogo.netlify.app/Imagens"
SITE = "https://www.zenithlacres.com.br"
CAT_JPG = f"{BASE}/Cat%C3%A1logo%20ZENITH%20capa.jpg"
CAT_PDF = f"{BASE}/Cat%C3%A1logo%20ZENITH.pdf"
WPP_NUM = "551120240427"

def wpp(msg):
    return f"https://api.whatsapp.com/send?phone={WPP_NUM}&text={urllib.parse.quote(msg)}"

WPP_GERAL    = wpp("Ola, gostaria de receber a tabela de precos dos lacres Zenith. Codigo ZENITH2026")
WPP_LACRES   = wpp("Ola, tenho interesse em lacres metalicos Zenith. Codigo ZENITH2026")
WPP_PLAST    = wpp("Ola, tenho interesse em lacres plasticos Zenith. Codigo ZENITH2026")
WPP_ABRAC    = wpp("Ola, tenho interesse em abracadeiras Zenith. Codigo ZENITH2026")
WPP_CAD      = wpp("Ola, tenho interesse em cadeados Zenith. Codigo ZENITH2026")
WPP_FITA     = wpp("Ola, tenho interesse em fitas Zenith. Codigo ZENITH2026")
WPP_MAL      = wpp("Ola, tenho interesse em malotes e pastas Zenith. Codigo ZENITH2026")
WPP_MAQ      = wpp("Ola, tenho interesse em maquinas lacradoras Zenith. Codigo ZENITH2026")
WPP_ESTOQUE  = wpp("Ola! Recebi o email da Zenith e quero verificar meu estoque para abril/maio. Pode me ajudar? Codigo ZENITH2026")
WPP_CATALOGO = wpp("Ola! Vi que tem novidades no catalogo Zenith 2026 e quero conhecer os novos itens. Codigo ZENITH2026")

# Produto: (nome, desc, img_url, wpp_url)
DESTAQUES = [
    ("Lacre Sextavado",   "Lider em seguranca industrial",  f"{BASE}/Lacres%20met%C3%A1licos/lacre-sextavado.png",   WPP_LACRES),
    ("Dupla Trava DT",    "Protecao inviolavel dupla",       f"{BASE}/Lacres%20Pl%C3%A1sticos/dupla-trava-dt.png",    WPP_PLAST),
    ("Abracadeira Nylon", "Alta resistencia, varios tamanhos",f"{BASE}/Abra%C3%A7adeiras/Abra%C3%A7adeira%20de%20Nylon%20%E2%80%94%20Padr%C3%A3o.png", WPP_ABRAC),
    ("Cadeado Tetra",     "Alta seguranca, chave exclusiva", f"{BASE}/Cadeados/Cadeado%20Tetra.png",                  WPP_CAD),
]

SECOES = [
    ("Lacres Metalicos", WPP_LACRES, [
        ("Lacre Sextavado",      "Robustez maxima, seguranca industrial",  f"{BASE}/Lacres%20met%C3%A1licos/lacre-sextavado.png"),
        ("ZPino Bolt Seal",      "Alta seguranca para containers",          f"{BASE}/Lacres%20met%C3%A1licos/zpino-bolt-seal.png"),
        ("Zlock Manivela",       "Fechamento pratico, resistente",          f"{BASE}/Lacres%20met%C3%A1licos/zlock-manivela.png"),
        ("Lacre Chumbo Sinete",  "Alta seguranca, uso fiscal",              f"{BASE}/Lacres%20met%C3%A1licos/lacre-chumbo-sinete.png"),
    ]),
    ("Lacres Plasticos", WPP_PLAST, [
        ("Lacre de Sacola Zni",  "Para lacracao de sacolas",                f"{BASE}/Lacres%20Pl%C3%A1sticos/Lacre%20de%20Sacola%20%E2%80%94%20Zni.png"),
        ("Dupla Trava DT",       "Protecao inviolavel dupla",               f"{BASE}/Lacres%20Pl%C3%A1sticos/dupla-trava-dt.png"),
        ("Anel Extintor",        "Normatizado para extintores",             f"{BASE}/Lacres%20Pl%C3%A1sticos/anel-extintor.png"),
        ("Lacre Ancora",         "Seguranca em caixas e bags",              f"{BASE}/Lacres%20Pl%C3%A1sticos/ancora.png"),
    ]),
    ("Abracadeiras", WPP_ABRAC, [
        ("Abracadeira Nylon",       "Alta resistencia, diversos tamanhos",  f"{BASE}/Abra%C3%A7adeiras/Abra%C3%A7adeira%20de%20Nylon%20%E2%80%94%20Padr%C3%A3o.png"),
        ("Abracadeira Metalica",    "Resistencia maxima, uso industrial",   f"{BASE}/Abra%C3%A7adeiras/Abra%C3%A7adeira%20Met%C3%A1lica.png"),
        ("Abracadeira Identificavel","Com espaco para identificacao",       f"{BASE}/Abra%C3%A7adeiras/Abra%C3%A7adeira%20Identific%C3%A1vel.png"),
        ("ZFIX Base Adesiva",       "Fixacao pratica para cabos",           f"{BASE}/Abra%C3%A7adeiras/ZFIX%20%E2%80%94%20Base%20Adesiva.png"),
    ]),
    ("Cadeados", WPP_CAD, [
        ("Cadeado Latao",        "Seguranca tradicional, varias medidas",   f"{BASE}/Cadeados/Cadeado%20Tradicional%20(lat%C3%A3o).png"),
        ("Cadeado Tetra",        "Alta seguranca, chave exclusiva",         f"{BASE}/Cadeados/Cadeado%20Tetra.png"),
        ("Cadeado Bloqueio",     "Bloqueio de energia LOTO/TAGOUT",         f"{BASE}/Cadeados/Cadeado%20Bloqueio.png"),
        ("Cadeado Colorido",     "Identificacao visual por cor",            f"{BASE}/Cadeados/Cadeado%20Colorido.png"),
    ]),
    ("Fitas", WPP_FITA, [
        ("Fita Adesiva",         "Alta aderencia, uso industrial",          f"{BASE}/Fitas/Fita%20adesiva.png"),
        ("Fita Isolante",        "Isolamento eletrico seguro",              f"{BASE}/Fitas/Fita%20isolante.png"),
        ("Fita Zebrada",         "Sinalizacao e demarcacao",                f"{BASE}/Fitas/Fita%20zebrada.png"),
        ("Fita Silver Tape",     "Alta resistencia, multiuso",              f"{BASE}/Fitas/Fita%20silver%20tape.png"),
    ]),
    ("Malotes e Pastas", WPP_MAL, [
        ("Malote Correio",       "Transporte seguro de documentos",         f"{BASE}/Malotes%2C%20pastas%20e%20bolsas/Malote%20Correio.png"),
        ("Pasta para Documentos","Organizacao e protecao",                  f"{BASE}/Malotes%2C%20pastas%20e%20bolsas/Pasta%20para%20Documentos.png"),
        ("Bolsa com Ziper",      "Estilo sacola, pratica e segura",         f"{BASE}/Malotes%2C%20pastas%20e%20bolsas/Bolsa%20com%20Z%C3%ADper%20(estilo%20Sacola).png"),
        ("Urna em Lona",         "Ideal para coletas e sorteios",           f"{BASE}/Malotes%2C%20pastas%20e%20bolsas/Urna%20em%20Lona.png"),
    ]),
    ("Maquinas", WPP_MAQ, [
        ("Lacradora Quadrada",   "Alta performance, robusta",               f"{BASE}/M%C3%A1quinas/M%C3%A1quina%20lacradora%20quadrada.png"),
        ("Maquina Seladora",     "Selagem rapida e segura",                 f"{BASE}/M%C3%A1quinas/M%C3%A1quina%20seladora.png"),
        ("Lacradora Redonda",    "Design compacto, eficiente",              f"{BASE}/M%C3%A1quinas/M%C3%A1quina%20lacradora%20redonda.png"),
        ("Refil de Selagem",     "Refil original para maquinas Zenith",     f"{BASE}/M%C3%A1quinas/Refil%20de%20selagem.png"),
    ]),
]

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
BTN_GREEN = "background:#25D366;color:#ffffff;text-decoration:none;font-weight:bold;font-size:14px;padding:12px 28px;display:inline-block;"
BTN_BLUE  = "background:#1F4E79;color:#ffffff;text-decoration:none;font-weight:bold;font-size:13px;padding:9px 18px;display:inline-block;"

def cta_row(label, url, bg="#25D366"):
    style = f"background:{bg};color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:13px 32px;display:inline-block;"
    return f"""  <tr>
    <td align="center" style="padding:20px 32px 8px 32px;">
      <a href="{url}" target="_blank" style="{style}">{label}</a>
    </td>
  </tr>"""

def destaque_card(nome, desc, img, url):
    return f"""<td width="50%" valign="top" style="padding:12px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid #d6e4f7;">
        <tr>
          <td align="center" valign="middle" height="160" style="background:#f4f7fb;padding:8px;height:160px;">
            <a href="{url}" target="_blank">
              <img src="{img}" alt="{nome}"
                style="display:block;border:0;width:auto;max-width:180px;max-height:144px;height:auto;margin:0 auto;">
            </a>
          </td>
        </tr>
        <tr>
          <td style="padding:10px 12px 14px 12px;">
            <p style="font-size:14px;font-weight:700;color:#1F4E79;margin:0 0 4px 0;line-height:1.4;">{nome}</p>
            <p style="font-size:12px;color:#666;margin:0 0 10px 0;line-height:1.5;">{desc}</p>
            <a href="{url}" target="_blank" style="{BTN_BLUE}">Solicitar cotacao</a>
          </td>
        </tr>
      </table>
    </td>"""

def produto_card(nome, desc, img, url, first=False):
    bl = "" if first else "border-left:1px solid #e0e8f4;"
    return f"""<td width="50%" valign="top" style="padding:12px;{bl}">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="center" valign="middle" height="160" style="background:#f4f7fb;padding:8px;height:160px;">
            <a href="{url}" target="_blank">
              <img src="{img}" alt="{nome}"
                style="display:block;border:0;width:auto;max-width:200px;max-height:144px;height:auto;margin:0 auto;">
            </a>
          </td>
        </tr>
      </table>
      <p style="font-size:13px;font-weight:700;color:#1F4E79;margin:8px 0 3px 0;line-height:1.4;">{nome}</p>
      <p style="font-size:12px;color:#666;margin:0 0 8px 0;line-height:1.5;">{desc}</p>
      <a href="{url}" target="_blank" style="{BTN_BLUE}">Solicitar cotacao</a>
    </td>"""

def section_block(titulo, wpp_url, produtos):
    rows_html = ""
    for i in range(0, len(produtos), 2):
        pair = produtos[i:i+2]
        c1 = produto_card(pair[0][0], pair[0][1], pair[0][2], wpp_url, first=True)
        c2 = produto_card(pair[1][0], pair[1][1], pair[1][2], wpp_url) if len(pair) > 1 else '<td width="50%"></td>'
        sep = "border-top:1px solid #e0e8f4;" if i > 0 else ""
        rows_html += f"""        <tr style="{sep}">{c1}{c2}</tr>\n"""
    cta_label = f"Falar com especialista em {titulo}"
    return f"""
  <!-- {titulo.upper()} -->
  <tr>
    <td style="padding:0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:24px;">
        <tr>
          <td style="background:#1F4E79;padding:10px 16px;">
            <p style="color:#FFD700;font-size:15px;font-weight:700;margin:0;line-height:1.4;">{titulo}</p>
          </td>
        </tr>
      </table>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid #e0e8f4;border-top:none;">
{rows_html}      </table>
    </td>
  </tr>
  {cta_row(cta_label, wpp_url)}"""

# ─────────────────────────────────────────────────────────────
# BLOCO ALERTA ESTOQUE ABRIL/MAIO
# ─────────────────────────────────────────────────────────────
estoque_block = f"""
  <!-- ALERTA ESTOQUE ABRIL/MAIO -->
  <tr>
    <td style="padding:16px 16px 0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#fff8e6;border:2px solid #e8a000;">
        <tr>
          <td style="background:#e8a000;padding:12px 20px;">
            <p style="margin:0;font-size:13px;font-weight:700;color:#ffffff;text-align:center;letter-spacing:1px;">&#9888; ABRIL &amp; MAIO &mdash; MESES DE ALTA DEMANDA &#9888;</p>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding:24px 32px 28px 32px;">
            <p style="font-size:22px;font-weight:700;color:#b35c00;margin:0 0 14px 0;text-align:center;line-height:1.3;">Seu estoque est&aacute; preparado<br>para os pr&oacute;ximos meses?</p>
            <p style="font-size:14px;color:#555;margin:0 0 10px 0;text-align:center;line-height:1.8;">
              Quem deixa pra verificar em cima da hora acaba pagando mais caro<br>ou &mdash; pior &mdash; <strong style="color:#b35c00;">para a opera&ccedil;&atilde;o por falta de material</strong>.
            </p>
            <p style="font-size:14px;color:#555;margin:0 0 22px 0;text-align:center;line-height:1.8;">
              Me conta como est&aacute; o seu estoque agora &mdash; assim a gente j&aacute;<br>
              te indica o que priorizar e garante prazo de entrega dentro do seu ritmo.
            </p>
            <a href="{WPP_ESTOQUE}" target="_blank"
              style="background:#e8a000;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:14px 36px;display:inline-block;">
              Verificar meu estoque com a Zenith
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>"""

# ─────────────────────────────────────────────────────────────
# BLOCO NOVIDADES NO CATALOGO
# ─────────────────────────────────────────────────────────────
novidades_block = f"""
  <!-- NOVIDADES CATALOGO 2026 -->
  <tr>
    <td style="padding:16px 16px 0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f0f6ff;border:2px solid #1F4E79;">
        <tr>
          <td style="background:#1F4E79;padding:12px 20px;">
            <p style="margin:0;font-size:13px;font-weight:700;color:#FFD700;text-align:center;letter-spacing:1px;">&#9733; CAT&Aacute;LOGO ZENITH 2026 &mdash; NOVOS ITENS DISPON&Iacute;VEIS &#9733;</p>
          </td>
        </tr>
        <tr>
          <td align="center" style="padding:24px 32px 28px 32px;">
            <p style="font-size:22px;font-weight:700;color:#1F4E79;margin:0 0 14px 0;text-align:center;line-height:1.3;">Tem coisa nova no cat&aacute;logo<br>que voc&ecirc; ainda n&atilde;o viu</p>
            <p style="font-size:14px;color:#555;margin:0 0 10px 0;text-align:center;line-height:1.8;">
              Adicionamos itens que nossos clientes pediam h&aacute; tempos &mdash; e que<br>
              j&aacute; est&atilde;o fazendo muita diferen&ccedil;a na opera&ccedil;&atilde;o de quem experimentou.
            </p>
            <p style="font-size:14px;color:#555;margin:0 0 22px 0;text-align:center;line-height:1.8;">
              D&aacute; uma olhada &mdash; pode ter exatamente o que falta<br>
              pra fechar o ciclo da sua opera&ccedil;&atilde;o com mais efici&ecirc;ncia.
            </p>
            <a href="{WPP_CATALOGO}" target="_blank"
              style="background:#1F4E79;color:#ffffff;text-decoration:none;font-weight:bold;font-size:15px;padding:14px 36px;display:inline-block;">
              Ver os novos itens do cat&aacute;logo
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>"""

# ─────────────────────────────────────────────────────────────
# DESTAQUE SECTION (2+2)
# ─────────────────────────────────────────────────────────────
dest_row1 = "".join(destaque_card(*d) for d in DESTAQUES[:2])
dest_row2 = "".join(destaque_card(*d) for d in DESTAQUES[2:])
destaques_block = f"""
  <!-- DESTAQUES -->
  <tr>
    <td style="padding:0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:24px;">
        <tr>
          <td style="background:#1F4E79;padding:10px 16px;">
            <p style="color:#FFD700;font-size:15px;font-weight:700;margin:0;">Destaques Zenith 2026</p>
          </td>
        </tr>
      </table>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid #e0e8f4;border-top:none;">
        <tr>{dest_row1}</tr>
        <tr style="border-top:1px solid #e0e8f4;">{dest_row2}</tr>
      </table>
    </td>
  </tr>"""

all_sections = destaques_block + cta_row("Receber tabela de precos completa", WPP_GERAL)
all_sections += "\n".join(section_block(t, w, p) for t, w, p in SECOES)

# ─────────────────────────────────────────────────────────────
# SOLUCOES POR SEGMENTO
# ─────────────────────────────────────────────────────────────
solucoes = """
  <!-- SEGMENTOS -->
  <tr>
    <td style="padding:0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:24px;background:#f0f6ff;border:1px solid #d0e4f7;">
        <tr>
          <td align="center" style="padding:20px;">
            <p style="font-size:16px;font-weight:700;color:#1F4E79;margin:0 0 16px 0;line-height:1.4;">Solucoes para o seu segmento</p>
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr><td style="padding:5px 0;font-size:14px;color:#333;line-height:1.5;">Transporte e logistica</td></tr>
              <tr><td style="padding:5px 0;font-size:14px;color:#333;line-height:1.5;">Correios e malotes</td></tr>
              <tr><td style="padding:5px 0;font-size:14px;color:#333;line-height:1.5;">Industria e manufactura</td></tr>
              <tr><td style="padding:5px 0;font-size:14px;color:#333;line-height:1.5;">Energia e utilities</td></tr>
              <tr><td style="padding:5px 0;font-size:14px;color:#333;line-height:1.5;">Varejo e supermercados</td></tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>"""

# ─────────────────────────────────────────────────────────────
# AUTORIDADE
# ─────────────────────────────────────────────────────────────
autoridade = """
  <!-- AUTORIDADE -->
  <tr>
    <td style="padding:0 16px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:20px;background:#1F4E79;">
        <tr>
          <td align="center" style="padding:24px 20px;">
            <p style="color:#FFD700;font-size:17px;font-weight:700;margin:0 0 16px 0;line-height:1.4;">Por que a Zenith?</p>
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td width="33%" align="center" style="padding:8px;">
                  <p style="color:#ffffff;font-size:22px;font-weight:700;margin:0;line-height:1.2;">500+</p>
                  <p style="color:#cce0ff;font-size:12px;margin:4px 0 0 0;line-height:1.4;">Produtos</p>
                </td>
                <td width="33%" align="center" style="padding:8px;border-left:1px solid #2d6aa0;border-right:1px solid #2d6aa0;">
                  <p style="color:#ffffff;font-size:22px;font-weight:700;margin:0;line-height:1.2;">20+</p>
                  <p style="color:#cce0ff;font-size:12px;margin:4px 0 0 0;line-height:1.4;">Anos de mercado</p>
                </td>
                <td width="33%" align="center" style="padding:8px;">
                  <p style="color:#ffffff;font-size:22px;font-weight:700;margin:0;line-height:1.2;">Brasil</p>
                  <p style="color:#cce0ff;font-size:12px;margin:4px 0 0 0;line-height:1.4;">Entrega nacional</p>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>"""

# ─────────────────────────────────────────────────────────────
# FULL HTML
# ─────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Zenith Lacres - Catalogo 2026</title>
</head>
<body style="margin:0;padding:0;background:#e6f0fa;font-family:Arial,Helvetica,sans-serif;">

<!-- PREHEADER INVISIVEL -->
<span style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;">Abril e maio sao meses de alta demanda - verifique seu estoque agora e confira os novos itens do catalogo Zenith 2026.</span>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#e6f0fa;">
<tr><td align="center" style="padding:20px 0;">

<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background:#ffffff;">

  <!-- HEADER -->
  <tr>
    <td style="background:#1F4E79;padding:20px 30px;">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td align="left" valign="middle">
            <img src="{BASE}/Logo%20zenith.png" alt="Zenith Lacres" width="160" height="45"
              style="display:block;border:0;width:160px;height:45px;filter:brightness(0) invert(1);">
            <p style="color:#cce0ff;font-size:12px;margin:6px 0 0 0;line-height:1.4;">Catalogo Industrial 2026 &bull; Lacres &bull; Abracadeiras &bull; Cadeados</p>
          </td>
          <td align="right" valign="middle">
            <a href="{WPP_GERAL}" target="_blank"
              style="background:#25D366;color:#ffffff;padding:10px 18px;font-size:14px;text-decoration:none;font-weight:bold;display:inline-block;">
              WhatsApp
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <!-- LINHA DOURADA -->
  <tr>
    <td height="4" style="background:#FFD700;font-size:0;line-height:0;">&nbsp;</td>
  </tr>

  <!-- BANNER -->
  <tr>
    <td>
      <a href="{SITE}" target="_blank">
        <img src="{BASE}/Banner.png" alt="Zenith Lacres - Solucoes profissionais" width="600"
          style="display:block;border:0;width:100%;max-width:600px;">
      </a>
    </td>
  </tr>

  <!-- PROPOSTA DE VALOR -->
  <tr>
    <td align="center" style="padding:28px 32px 8px 32px;">
      <p style="font-size:21px;font-weight:700;color:#1F4E79;margin:0 0 10px 0;text-align:center;line-height:1.3;">Seguranca logistica para a sua operacao</p>
      <p style="font-size:14px;color:#444;margin:0;text-align:center;line-height:1.6;">
        Lacres, abracadeiras, cadeados e solucoes completas para transporte e industria.<br>
        Informe o codigo <strong style="color:#1F4E79;">#ZENITH2026</strong> e receba condicoes especiais.
      </p>
    </td>
  </tr>

  {cta_row("Receber tabela de precos", WPP_GERAL)}

  {estoque_block}

  {novidades_block}

  {all_sections}

  {solucoes}

  {cta_row("Falar com especialista Zenith", WPP_GERAL)}

  {autoridade}

  <!-- CATALOGO -->
  <tr>
    <td align="center" style="padding:32px 32px 8px 32px;">
      <p style="font-size:16px;font-weight:700;color:#1F4E79;margin:0 0 12px 0;text-align:center;line-height:1.4;">
        Mais de 500 produtos no catalogo completo
      </p>
      <a href="{CAT_JPG}" target="_blank">
        <img src="{CAT_JPG}" alt="Catalogo Zenith" width="400"
          style="display:block;border:0;width:100%;max-width:400px;margin:0 auto 16px auto;">
      </a>
      <a href="{CAT_PDF}" target="_blank"
        style="background:#1F4E79;color:#ffffff;text-decoration:none;font-size:14px;font-weight:700;padding:12px 28px;display:inline-block;">
        Acessar Catalogo Completo (PDF)
      </a>
    </td>
  </tr>

  {cta_row("Solicitar cotacao agora", WPP_GERAL)}

  <!-- RODAPE -->
  <tr>
    <td height="20" style="font-size:0;line-height:0;">&nbsp;</td>
  </tr>
  <tr>
    <td align="center" style="background:#1F4E79;padding:24px 32px;">
      <img src="{BASE}/Logo%20zenith.png" alt="Zenith Lacres" width="120" height="34"
        style="display:block;border:0;margin:0 auto 12px auto;filter:brightness(0) invert(1);">
      <p style="color:#ffffff;font-size:13px;margin:0 0 6px 0;text-align:center;line-height:1.5;">
        Zenith Lacres - Seguranca, padronizacao e confianca
      </p>
      <p style="color:#cce0ff;font-size:12px;margin:0 0 14px 0;text-align:center;line-height:1.5;">
        R. Constantino Fusco, 256 - Vila Formosa, Sao Paulo - SP, 03383-070
      </p>
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">
        <tr>
          <td style="padding:0 10px;">
            <a href="{SITE}" target="_blank" style="color:#FFD700;text-decoration:none;font-size:13px;font-weight:700;">Site</a>
          </td>
          <td style="color:#cce0ff;font-size:13px;">|</td>
          <td style="padding:0 10px;">
            <a href="{WPP_GERAL}" target="_blank" style="color:#FFD700;text-decoration:none;font-size:13px;font-weight:700;">WhatsApp</a>
          </td>
          <td style="color:#cce0ff;font-size:13px;">|</td>
          <td style="padding:0 10px;">
            <a href="{CAT_PDF}" target="_blank" style="color:#FFD700;text-decoration:none;font-size:13px;font-weight:700;">Catalogo PDF</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>

</table>

</td></tr>
</table>

</body>
</html>"""

with open("index.html", "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

size_kb = len(html.encode("utf-8")) / 1024
print(f"Arquivo gerado: {size_kb:.1f} KB")
print(f"Tags script: {html.count('<script')}")
print(f"Tag style block: {html.count('<style')}")
print(f"object-fit: {html.count('object-fit')}")
print(f"Links WPP: {html.count('api.whatsapp.com')}")
