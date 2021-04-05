import json

data = '{"firstname":"elif","lastname":"secgin"}'
y = json.loads(data)

customer = {
    "firstname":"elif",
    "lastname":"secgin"
}
customerJson = json.dumps(customer)
print(customer)

print(json.dumps("elif"))