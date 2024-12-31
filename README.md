# API-Architect 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-green.svg)](https://fastapi.tiangolo.com/)

API-Architect is an intelligent automation tool that streamlines the process of creating, documenting, and maintaining REST APIs. Using OpenAI's GPT models, it analyzes your project structure and automatically generates production-ready API endpoints, documentation, and test cases.

## 🌟 Features

- 🔄 Automated API endpoint generation
- 📝 OpenAPI specification management
- 🧪 Automated test case generation
- 🔍 Project structure analysis
- 🔧 Git integration
- 📊 Comprehensive logging system
- ⚙️ Configuration management

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/api-architect.git
cd api-architect

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

1. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

2. Run API-Architect:
```bash
python api_architect.py --project-path /path/to/your/project --openai-key $OPENAI_API_KEY
```

## 📁 Project Structure

```
your-project/
├── api/
│   └── endpoints/
│       └── generated_endpoints.py
├── tests/
│   └── test_api.py
├── api_architect_config.json
└── api_architect.log
```

## 🛠️ Configuration

API-Architect uses a configuration file (`api_architect_config.json`) to store project settings and OpenAPI specifications. The file is automatically generated and updated during the tool's operation.

## 🧪 Testing

```bash
# Run tests
pytest tests/
```

## 📖 Documentation

Generated API documentation will be available at:
- OpenAPI UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT models
- FastAPI framework
- All contributors who help improve this project

## 📫 Contact

Your Name - [@AlhuwaidiNora](alhuwaidinr@gmail.com)

Project Link: [(https://github.com/AlhuwaidiNora/Api-Architect.gi)]
