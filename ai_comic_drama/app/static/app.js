async function submitStory() {
    const titleInput = document.getElementById("title");
    const contentInput = document.getElementById("content");
    const statusEl = document.getElementById("status");
    const resultEl = document.getElementById("result");
    const taskIdEl = document.getElementById("task-id");
    const taskStatusEl = document.getElementById("task-status");
    const videoUrlEl = document.getElementById("video-url");
    const button = document.getElementById("submit-btn");

    const content = contentInput.value.trim();
    const title = titleInput.value.trim();

    if (!content) {
        statusEl.textContent = "请先输入故事内容。";
        return;
    }

    button.disabled = true;
    statusEl.textContent = "正在调用后端服务生成漫剧视频，请稍候...";
    resultEl.style.display = "none";

    try {
        const response = await fetch("/api/v1/story/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: title || null,
                content: content,
            }),
        });

        if (!response.ok) {
            statusEl.textContent = "请求失败，请稍后重试。";
            button.disabled = false;
            return;
        }

        const data = await response.json();

        taskIdEl.textContent = data.task_id;
        taskStatusEl.textContent = data.status;
        videoUrlEl.textContent = data.video_url || "暂未生成视频地址";

        resultEl.style.display = "block";
        statusEl.textContent = "生成完成。";
    } catch (error) {
        statusEl.textContent = "调用接口时发生错误，请检查控制台。";
        console.error(error);
    } finally {
        button.disabled = false;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("submit-btn");
    button.addEventListener("click", submitStory);
});

