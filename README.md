# Morse Code MCP Server

这是一个基于Python的摩尔斯电码服务器项目，提供摩尔斯电码的编码和解码功能。

## 功能特点

- 支持文本到摩尔斯电码的转换
- 支持摩尔斯电码到文本的转换
- RESTful API接口
- 简单易用的Web界面

## 安装说明

1. 克隆项目
```bash
git clone https://github.com/lqycoding/morsecode-mcp-server.git
cd morsecode-mcp-server
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行服务器
```bash
python app.py
```

## API文档

### POST /encode
将文本转换为摩尔斯电码

### POST /decode
将摩尔斯电码转换为文本

## 开发环境

- Python 3.8+
- Flask 3.0.2
- 其他依赖请参考 requirements.txt

## 许可证

MIT License