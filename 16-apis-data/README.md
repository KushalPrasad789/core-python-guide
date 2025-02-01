# 🌐 Python APIs & Data: Fetch, Process, and Secure Data

Learn to interact with REST/GraphQL APIs, handle JSON/XML, and build robust data pipelines.  

---

## 🧩 APIs & Data Cheat Sheet  
| Tool | Syntax | Purpose |  
|------|--------|---------|  
| **`requests`** | `requests.get(url)` | Simple HTTP requests |  
| **`aiohttp`** | `async with session.get(url)` | Async HTTP requests |  
| **`json`** | `json.loads(data)` | Parse JSON data |  
| **`xml.etree`** | `ET.parse("data.xml")` | Parse XML data |  
| **`pydantic`** | `BaseModel` | Validate API responses |  
| **`requests-cache`** | `CachedSession()` | Cache API responses |  

---

## 🚨 Common Pitfalls & Fixes  
### 1. **Hardcoding API Keys**  
```python  
API_KEY = "12345"  # Exposed in code!  
```  
✅ **Fix**: Use environment variables:  
```python  
import os  
API_KEY = os.environ["API_KEY"]  
```  

### 2. **Ignoring Rate Limits**  
```python  
for _ in range(1000):  
    requests.get("https://api.example.com/data")  # Risk of ban!  
```  
✅ **Fix**: Add delays or use `tenacity` for backoff:  
```python  
from tenacity import retry, wait_exponential  

@retry(wait=wait_exponential(multiplier=1, min=2, max=10))  
def safe_request():  
    requests.get(...)  
```  

### 3. **Unvalidated API Responses**  
```python  
data = response.json()  
print(data["missing_key"])  # KeyError!  
```  
✅ **Fix**: Validate with `pydantic`:  
```python  
class ResponseModel(BaseModel):  
    required_key: str  

validated = ResponseModel(**data)  
```  

---

## 🔍 Core Concepts  
### **HTTP Methods & Status Codes**  
| Method | Use Case | Status | Meaning |  
|--------|----------|--------|---------|  
| `GET` | Fetch data | 200 | OK |  
| `POST` | Create data | 201 | Created |  
| `PUT` | Update data | 204 | No Content |  
| `DELETE` | Remove data | 404 | Not Found |  

### **JSON vs XML**  
| Feature | JSON | XML |  
|---------|------|-----|  
| **Syntax** | `{"key": "value"}` | `<key>value</key>` |  
| **Readability** | High | Verbose |  
| **Use Case** | APIs | Legacy systems |  

---

## 🌍 Real-World Scenarios  
### 1. **Weather CLI with OpenWeatherMap API**  
```python  
import requests  

def get_weather(city):  
    API_KEY = os.environ["OWM_API_KEY"]  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"  
    response = requests.get(url)  
    return response.json()["main"]["temp"]  

print(f"Temperature: {get_weather('London')}K")  
```  

### 2. **Async GitHub API Pagination**  
```python  
import aiohttp  
import asyncio  

async def fetch_github_repos(username):  
    async with aiohttp.ClientSession() as session:  
        repos = []  
        page = 1  
        while True:  
            url = f"https://api.github.com/users/{username}/repos?page={page}"  
            async with session.get(url) as response:  
                data = await response.json()  
                if not data:  
                    break  
                repos.extend(data)  
                page += 1  
        return repos  

asyncio.run(fetch_github_repos("torvalds"))  
```  

### 3. **Streaming Data with WebSockets**  
```python  
import websockets  
import asyncio  

async def listen_to_stream():  
    async with websockets.connect("wss://stream.example.com") as ws:  
        while True:  
            data = await ws.recv()  
            print(f"Received: {data}")  

asyncio.run(listen_to_stream())  
```  

---

## 💡 Advanced Features  
### **OAuth2 Authentication**  
```python  
from requests_oauthlib import OAuth2Session  

client_id = os.environ["CLIENT_ID"]  
client_secret = os.environ["CLIENT_SECRET"]  

oauth = OAuth2Session(client_id, redirect_uri="https://callback.com")  
authorization_url, _ = oauth.authorization_url("https://auth.example.com")  
print(f"Authorize here: {authorization_url}")  

# After user grants access:  
token = oauth.fetch_token("https://auth.example.com/token", client_secret=client_secret)  
response = oauth.get("https://api.example.com/user")  
```  

### **GraphQL API Client**  
```python  
from gql import gql, Client  
from gql.transport.requests import RequestsHTTPTransport  

transport = RequestsHTTPTransport(url="https://api.example.com/graphql")  
client = Client(transport=transport)  

query = gql("""  
    query GetUser($id: ID!) {  
        user(id: $id) {  
            name  
            email  
        }  
    }  
""")  

result = client.execute(query, variable_values={"id": 1})  
```  

### **Caching API Responses**  
```python  
from requests_cache import CachedSession  

session = CachedSession("api_cache", expire_after=3600)  # Cache for 1 hour  
response = session.get("https://api.example.com/stable-data")  
```  

---

## ✅ Try It Yourself!  
1. **Stock Price CLI**:  
   Use the Alpha Vantage API to fetch real-time stock prices.  

2. **GraphQL Pagination**:  
   Implement cursor-based pagination for a GraphQL query.  

3. **Secure Key Storage**:  
   Encrypt API keys using `cryptography` and load them at runtime.  

---

## 📚 Resources  
- **OAuth2 Guide**: [Auth0 Docs](https://auth0.com/docs/get-started/authentication-and-authorization-flow)  
- **GraphQL Tutorial**: [How to GraphQL](https://www.howtographql.com/)  

---

## ➡️ What’s Next?  
Ready to manage dependencies with **Virtual Environments**? Head over to [17-virtual-environments](/17-virtual-environments)!  
