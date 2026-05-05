from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

length_conversion_factors = {
    'mm' : 1/1000,
    'cm' : 1/100,
    'm' : 1,
    'km' : 1000,
    'in' : 0.0254,
    'ft' : 0.3048,
    'yd' : 0.9144,
    'mi' : 1609.34,
}

weight_conversion_factors = {
    'mg' : 1/1000000,
    'g' : 1/1000,
    'kg' : 1,
    'oz' : 0.0283495,
    'lb' : 0.453592,
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context={}
    )

@app.get("/length_conversion")
def length_conversion(conversion_from, conversion_to, input_value: float):
    result = input_value * length_conversion_factors[conversion_from] / length_conversion_factors[conversion_to]
    return {"result": result}

@app.get("/weight_conversion")
def weight_conversion(conversion_from, conversion_to, input_value: float):
    result = input_value * weight_conversion_factors[conversion_from] / weight_conversion_factors[conversion_to]
    return {"result": result}

@app.get("/temperature_conversion")
def temperature_conversion(conversion_from, conversion_to, input_value: float):

    if conversion_from == conversion_to:
        return {"result": input_value}

    def c_to_f(c):
        return c * 9/5 + 32
    def f_to_c(f):
        return (f - 32) * 5/9
    def c_to_k(c):
        return c + 273.15
    def k_to_c(k):
        return k - 273.15
    def f_to_k(f):
        return c_to_k(f_to_c(f))
    def k_to_f(k):
        return c_to_f(k_to_c(k))

    functions = {
            '°C_to_°F': c_to_f,
            '°F_to_°C': f_to_c,
            '°C_to_K': c_to_k,
            'K_to_°C': k_to_c,
            '°F_to_K': f_to_k,
            'K_to_°F': k_to_f,
        }

    key = conversion_from + "_to_" + conversion_to

    return {"result": functions[key](input_value)}
