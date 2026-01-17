# AI漫剧自动化

## 本地运行指南

### 1. 环境准备

- Python 版本：建议 3.9+  
- 安装依赖（至少需要 FastAPI 和 Uvicorn）：

```bash
pip install fastapi uvicorn[standard]
```

如需运行测试，可以额外安装：

```bash
pip install pytest
```

### 2. 启动 FastAPI 服务

在项目根目录 `AIComicDrama` 下运行：

```bash
uvicorn ai_comic_drama.app.main:app --reload
```

启动成功后，可以访问：

- 文档页面（Swagger）：`http://127.0.0.1:8000/docs`

### 3. 接口快速体验

1. 提交故事
   - 方法：`POST`
   - 地址：`http://127.0.0.1:8000/api/v1/story/`
   - 请求示例：

   ```json
   {
     "title": "山里的奇遇",
     "content": "从前有座山，山里有个小村庄，小孩想成为勇者……",
     "tone": "热血",
     "target_length": 5
   }
   ```

   - 响应示例（当前为占位实现，任务状态固定为 pending）：

   ```json
   {
     "task_id": "task-123456789",
     "status": "pending",
     "message": null
   }
   ```

2. 查询任务状态
   - 方法：`GET`
   - 地址：`http://127.0.0.1:8000/api/v1/story/{task_id}`
   - 示例：`http://127.0.0.1:8000/api/v1/story/task-123456789`

   - 响应示例：

   ```json
   {
     "task_id": "task-123456789",
     "status": "pending",
     "message": null
   }
   ```

> 说明：目前任务状态和脚本生成逻辑仍是最小可运行占位实现，主要用于验证接口和整体项目结构是否工作正常。后续会逐步接入真实的文案创作、分镜设计、图片生成和视频合成流程。
