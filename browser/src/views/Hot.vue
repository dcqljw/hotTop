<template>
  <div class="hot">
    <el-card class="box-card hot-card" shadow="always">
      <template #header>
        <img src="https://www.baidu.com/favicon.ico" style="height: 26px">
        <span class="hot-card-title">百度热搜</span>
      </template>
      <div v-for="item in baidu" :key="item.idx" class="hot-item">
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
    <el-card class="box-card hot-card" shadow="always">
      <template #header>
        <img src="https://static.zhihu.com/heifetz/favicon.ico" style="height: 26px">
        <span class="hot-card-title">知乎热搜</span>
      </template>
      <div v-for="item in zhihu" :key="item.idx" class="hot-item">
        <div class="top-item">
          <span v-if="item.idx === 1" class="no1 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx ===2" class="no2 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 3" class="no3 no">
            {{ item.idx }}</span>
          <span v-else class="no">
            {{ item.idx }}</span>
          <el-link :href="item.url" target="_blank" :underline="false">{{ item.title }}</el-link>
        </div>
      </div>
    </el-card>
    <el-card class="box-card hot-card" shadow="always">
      <template #header>
        <img src="https://static.hdslb.com/images/favicon.ico" style="height: 26px">
        <span class="hot-card-title">哔哩哔哩热搜</span>
      </template>
      <div v-for="item in bilibili" :key="item.idx" class="hot-item">
        <div class="top-item">
          <span v-if="item.idx === 1" class="no1 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 2" class="no2 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 3" class="no3 no">
            {{ item.idx }}</span>
          <span v-else class="no">
            {{ item.idx }}</span>
          <el-link :underline="false" target="_blank" :href="item.url">{{ item.title }}</el-link>
        </div>
      </div>
    </el-card>
    <el-card class="box-card hot-card" shadow="always">
      <template #header>
        <img src="https://weibo.com/favicon.ico" style="height: 26px">
        <span class="hot-card-title">微博热搜</span>
      </template>
      <div v-for="item in biliTop" :key="item.idx" class="hot-item">
        <div class="top-item">
          <span v-if="item.idx === 1" class="no1 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 2" class="no2 no">
            {{ item.idx }}</span>
          <span v-else-if="item.idx === 3" class="no3 no">
            {{ item.idx }}</span>
          <span v-else class="no">
            {{ item.idx }}</span>
          <el-link :underline="false" target="_blank" :href="item.url">{{ item.title }}</el-link>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Hot",
  data() {
    return {
      baidu: [],
      zhihu: [],
      bilibili: [],
      weibo: [],
      biliTop: [],
      loading: true,
      dialogVisible: false,
      url: "",
    }
  },
  created() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/api/hot"
    axios.defaults.method = "get"
    axios({
      params: {
        source: "baidu"
      }
    }).then(res => {
      console.log(res)
      this.baidu = res.data.data
      this.loading = false
    })
    axios({
      params: {
        source: "zhihu"
      }
    }).then(res => {
      this.zhihu = res.data.data
    })
    axios({
      params: {
        source: "bilibili"
      }
    }).then(res => {
      this.bilibili = res.data.data
    })
    axios({
      params: {
        source: "weibo"
      }
    }).then(res => {
      this.weibo = res.data.data
    })
    axios({
      params: {
        source: "biliTop"
      }
    }).then(res => {
      this.biliTop = res.data.data
    })
    document.title = "hot"
    console.log(this.zhihu)
  },
  methods: {
    toHref(url) {
      this.url = url
      this.dialogVisible = true
    }
  }
}
</script>

<style scoped>
.hot {
  position: fixed;
  top: 50px;
  height: 350px;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}

.hot-card {
  width: 400px;
}

.top-item {
  display: flex;;
}

.hot-item {
  margin: 10px 0;
}

.hot-card /deep/ .el-card__header {
  padding: 10px;
}

.hot-card /deep/ .el-card__header div {
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

.hot-card /deep/ .el-link {
  display: block;
  width: 340px;
}

.hot-card /deep/ .el-card__body {
  padding: 0 10px;
}

.hot-card /deep/ .el-card__body {
  overflow-y: scroll;
  height: 290px;
}

.hot-card /deep/ .el-card__body::-webkit-scrollbar {
  width: 5px;
}

/* 滚动槽 */
.hot-card /deep/ .el-card__body::-webkit-scrollbar-track {
  border-radius: 10px;
}

/* 滚动条滑块 */
.hot-card /deep/ .el-card__body::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: rgba(130, 130, 130, .5);
}


.no {
  width: 22px;
  height: 22px;
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

.hot /deep/ .el-dialog {
  margin-top: 0 !important;
  width: 50%;
  position: fixed;
  height: 95%;
  left: 20%;
  top: 10px;
}

.hot /deep/ .el-dialog__body {
  height: 100%;
  padding: 0;
}

.hot /deep/ .el-dialog__header {
  padding: 0;
}

.hot /deep/ .el-dialog__headerbtn {
  height: 50px;
  width: 50px;
  right: -100px;
  font-size: 34px;
  border-radius: 34px;
  background-color: #000;
  opacity: .6;
}
</style>