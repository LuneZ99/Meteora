# Meteora

基于 mirai-http 的 qq-bot，是 [ErGo](https://github.com/corgiclub/ErGo) 的稳定版。

名字来源于《Re: Creators》中的 メテオラ<sup>Meteora</sup>・エスターライヒ<sup>Österreich</sup>



> *世界は選択と覚悟を要求する。*
>
> *The world requires choice and resolution.*
>
> *世界迫使人做出选择与觉悟。*

## Bot 功能

###### 所有功能均可定制 / 可选开启

- 💬 关键词回复
- 🧠 AI 续写（基于 CPM-LM）
- 🖇 视频信息查询（ ✅ Bilibili / ➖ youtube）
- 📰 今日要闻
- ~~📃 聊天记录存储至数据库~~
- 💾 系统信息 / 状态查询
- 新功能开发中………
- pixiv 搜图 / 查图 / 跟踪动态
- Twitter 搜图 / 查图 / 跟踪动态
- 翻译
- 

## 运行方法

#### 直接添加 qq号 1206565965 启用（测试中，请在添加后私聊）。

或本地编译：

build bot 所需 docker 镜像: `cd script/docker-image; sh docker-build.sh`

运行 bot 容器并启动 bot: `sh scripts/docker-start-bot.sh`

仅运行 bot 容器环境(debug 使用): `sh scripts/docker-run.sh`

接入正在运行的 bot 容器: `docker attach ergo-bot-container`

退出正在运行的 bot 容器（不可直接 ctrl+c 或 ctrl+d）: ctrl+p ctrl+q



