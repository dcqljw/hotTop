<template>
  <div class="hot">
    <el-card v-for="result in data" :key="result" class="box-card hot-card" shadow="always">
      <template #header>
        <img :src="logoUrl[result['name']]" style="height: 26px">
        <span class="hot-card-title">{{ hot_china[result["name"]] }}</span>
      </template>
      <div v-for="item in result['data']" :key="item" class="hot-item">
        <div class="top-item">
          <span v-if="item.idx === 1" class="no1 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 2" class="no2 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 3" class="no3 no">
            {{ item.idx }}</span>
          <span v-else class="no">
            {{ item.idx }}</span>
          <el-link :href="item.url" target="_blank" :underline="false">{{ item.title }}</el-link>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";
import md5 from "js-md5"

export default {
  name: "Hot",
  data() {
    return {
      data: [],
      logoUrl: {
        "zhihu": "https://static.zhihu.com/heifetz/favicon.ico",
        "baidu": "https://www.baidu.com/favicon.ico",
        "bilibili": "https://static.hdslb.com/images/favicon.ico",
        "weibo": "https://weibo.com/favicon.ico",
        "biliTop": "https://static.hdslb.com/images/favicon.ico"
      },
      hot: ["baidu", "zhihu", "bilibili", "weibo"],
      hot_china: {
        "baidu": "百度",
        "zhihu": "知乎",
        "bilibili": "B站",
        "weibo": "微博",
        "biliTop": "B站日榜"
      }
    }
  },
  methods: {},
  created() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/api/get_all_hot"
    axios.defaults.method = "post"
    let _t = Date.parse(new Date())
    let time = _t.toString().substring(0, _t.toString().length - 3)
    console.log(md5(time))
    axios({
      data: {
        t: time,
        sign: md5(time)
      }
    }).then(res => {
      if (res.status !== 200) {
        this.$message.error("请求失败")
      } else {
        this.data = res.data.data
      }
    })
  },
}
</script>

<style scoped>
.hot {
  flex-wrap: wrap;
  margin: 0 auto;
  justify-content: center;
  display: flex;
}

.hot > div {
  margin: 10px 20px;
}

.hot-card {
  width: 400px;
  height: 350px;
}

.top-item {
  display: flex;;
}

.hot-item {
  margin: 10px 0;
}


.hot-card :deep(.el-card__header) {
  display: flex;
  padding: 10px;
}

.hot-card :deep(.el-card__header div) {
  display: flex;
  position: relative;
}

.hot-card-title {
  line-height: 26px;
  margin-left: 10px;
}

.toHistory {
  position: absolute;
  right: 10px;
  line-height: 26px;
  width: auto !important;
}

.hot-card :deep(.el-link) {
  display: block;
  width: 340px;
}

.hot-card :deep(.el-card__body ) {
  padding: 0 10px;
}

.hot-card :deep(.el-card__body) {
  overflow-y: scroll;
  height: 290px;
}

.hot-card :deep(.el-card__body::-webkit-scrollbar) {
  width: 5px;
}

/* 滚动槽 */
.hot-card :deep(.el-card__body::-webkit-scrollbar-track) {
  border-radius: 10px;
}

/* 滚动条滑块 */
.hot-card :deep(.el-card__body::-webkit-scrollbar-thumb) {
  border-radius: 10px;
  background: rgba(130, 130, 130, .5);
}


.no {
  width: fit-content;
  font-size: 10px;
  padding: 1px 6px;
  height: 18px;
  text-align: center;
  border-radius: 5px;
  margin-right: 5px;
  background-color: rgba(124, 124, 124, 0.3);
}

.no1 {
  background: #f1404b;
  color: white;
}

.no2 {
  background-color: #c56831;
  color: white;
}

.no3 {
  background-color: #b89e2c;
  color: white;
}

.hot :deep(.el-dialog) {
  margin-top: 0 !important;
  width: 50%;
  position: fixed;
  height: 95%;
  left: 20%;
  top: 10px;
}

.hot :deep(.el-dialog__body) {
  height: 100%;
  padding: 0;
}

.hot :deep(.el-dialog__header) {
  padding: 0;
}

.hot :deep(.el-dialog__headerbtn) {
  height: 50px;
  width: 50px;
  right: -100px;
  font-size: 34px;
  border-radius: 34px;
  background-color: #000;
  opacity: .6;
}
</style>