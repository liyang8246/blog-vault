---
date: 2025-12-18
tags:
  - frontend
  - tutorial
  - vue
description: Vue 3 使用 MutationObserver 实现内容变化时自动滚动到底部, 确保最新内容始终可见, 简单实用的前端解决方案.
---
原理很简单 当容器内的内容发生变化时，MutationObserver 会检测到 DOM 的变化，然后自动触发 `scrollToBottom` 函数，将滚动条移动到最底部，确保最新内容始终可见。

```vue
<script setup lang="ts">
const container = ref<HTMLElement>()
let observer: MutationObserver | null = null

const scrollToBottom = () => {
  container.value!.scrollTop = container.value!.scrollHeight
}

onMounted(() => {
  observer = new MutationObserver(scrollToBottom)
  observer.observe(container.value!, {
    childList: true,
    subtree: true,
  })
  scrollToBottom()
})

onUnmounted(() => {
  observer?.disconnect()
})
</script>

<template>
  <div
    ref="container"
    class="scroll-container"
  >
    <slot />
  </div>
</template>
```
