# ShortChain 项目

这是一个基于 FastAPI 框架开发的 Web 应用程序，提供了用户认证、数据库操作等功能。

## 项目结构

```
shortChain/
├── api/                # API 路由层
├── config/            # 配置文件
├── db/                # 数据库相关
├── dependencies/      # 依赖注入
├── models/           # 数据模型
├── schemes/          # 数据模式
├── servies/          # 业务逻辑层
├── utils/            # 工具函数
├── app.py            # 应用主文件
└── main.py           # 入口文件
```

## 主要功能

- 用户认证系统（基于 JWT）
- 数据库操作（使用 SQLAlchemy）
- 密码加密（使用 bcrypt）
- 依赖注入系统

## 技术栈

- FastAPI
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)
- Pydantic

## 安装步骤

1. 克隆项目
```bash
git clone [项目地址]
cd shortChain
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install python-multipart
```

## 运行项目

```bash
uvicorn main:app --reload
```

## 主要特性

### 认证系统
- 使用 JWT 进行用户认证
- 密码使用 bcrypt 加密
- Token 有效期为 30 分钟

### 数据库
- 使用 SQLAlchemy 进行数据库操作
- 支持异步操作
- 自动会话管理

### 依赖注入
- 统一的依赖管理
- 数据库会话自动注入
- 认证中间件

## API 文档

启动服务后，可以访问以下地址查看 API 文档：
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 安全特性

- 密码加密存储
- JWT 令牌认证
- 请求验证
- 异常处理

## 开发指南

1. 添加新的 API 路由：
   - 在 `api` 目录下创建新的路由文件
   - 在 `app.py` 中注册路由

2. 添加新的数据模型：
   - 在 `models` 目录下创建新的模型文件
   - 在 `schemes` 目录下创建对应的 Pydantic 模型

3. 添加新的业务逻辑：
   - 在 `servies` 目录下创建新的服务文件
   - 在路由中注入服务

## 注意事项

- 请确保在生产环境中修改 `SECRET_KEY`
- 建议使用环境变量管理敏感配置
- 定期更新依赖包以修复安全漏洞

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

[添加许可证信息] 
