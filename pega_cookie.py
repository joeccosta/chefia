#!/usr/bin/env python3
# criado por Joe Costa em 09/01/2026
# Version 0.03

import argparse
import subprocess
import sys
import browser_cookie3


def copy_cookie(domain, cookie_name):
    try:
        cookies = browser_cookie3.firefox(domain_name=domain)
    except Exception as e:
        print(f"Erro ao acessar cookies do Firefox: {e}", file=sys.stderr)
        sys.exit(1)

    for c in cookies:
        if c.name == cookie_name:
            subprocess.run(
                ["xclip", "-selection", "clipboard"],
                input=c.value,
                text=True,
                check=True
            )
            print(f"Cookie '{cookie_name}' copiado para a área de transferência.")
            return

    print(f"Cookie '{cookie_name}' não encontrado para o domínio '{domain}'.", file=sys.stderr)
    sys.exit(2)


def main():
    parser = argparse.ArgumentParser(
        description="Copia o valor de um cookie do Firefox para a área de transferência (X11)."
    )
    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Domínio do cookie (ex: .dti.ufmg.br)"
    )
    parser.add_argument(
        "-c", "--cookie",
        default="SESSION",
        help="Nome do cookie (padrão: SESSION)"
    )

    args = parser.parse_args()
    copy_cookie(args.domain, args.cookie)


if __name__ == "__main__":
    main()
