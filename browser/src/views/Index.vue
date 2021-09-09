<template>
  <img class="background" :src="image['url']">
  <div class="rightTop">
    <div class="user" @click="showUser">
      <svg t="1631181534514" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
           p-id="3496" width="200" height="200">
        <path
            d="M856.339597 799.428571q0 62.285714-35.714286 106.857143t-86 44.571429H246.625311q-50.285714 0-86-44.571429T124.911026 799.428571q0-48.571429 4.857143-91.714285t18-86.857143 33.428571-74.857143 53.714286-50.857143T311.768169 475.428571q74.857143 73.142857 178.857142 73.142858t178.857143-73.142858q43.428571 0 76.857143 19.714286t53.714286 50.857143 33.428571 74.857143 18 86.857143 4.857143 91.714285z m-146.285714-506.857142q0 90.857143-64.285714 155.142857T490.625311 512 335.482454 447.714286 271.19674 292.571429t64.285714-155.142858T490.625311 73.142857t155.142858 64.285714T710.053883 292.571429z"
            p-id="3497" fill="#707070"></path>
      </svg>
    </div>
    <div class="settings" @click="showSetings">
      <svg t="1631181335418" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
           p-id="2201" width="200" height="200">
        <path
            d="M896 628.48l-34.133333-28.16a85.333333 85.333333 0 0 1-30.72-69.973333V512v-18.346667a85.333333 85.333333 0 0 1 30.72-69.973333l34.133333-28.16A42.666667 42.666667 0 0 0 906.24 341.333333l-49.493333-85.333333a42.666667 42.666667 0 0 0-51.626667-18.346667l-42.666667 15.36a85.333333 85.333333 0 0 1-75.946666-8.106666 233.813333 233.813333 0 0 0-31.573334-18.346667 85.333333 85.333333 0 0 1-45.226666-61.866667l-7.253334-42.666666a42.666667 42.666667 0 0 0-42.666666-35.84h-98.133334a42.666667 42.666667 0 0 0-42.666666 35.84l-7.253334 42.666666a85.333333 85.333333 0 0 1-43.52 61.866667 233.813333 233.813333 0 0 0-31.573333 18.346667 85.333333 85.333333 0 0 1-75.946667 8.106666l-42.666666-15.36A42.666667 42.666667 0 0 0 167.253333 256L117.76 341.333333A42.666667 42.666667 0 0 0 128 395.52l34.133333 28.16a85.333333 85.333333 0 0 1 30.72 69.973333v36.693334a85.333333 85.333333 0 0 1-30.72 69.973333l-34.133333 28.16A42.666667 42.666667 0 0 0 117.76 682.666667l49.493333 85.333333a42.666667 42.666667 0 0 0 51.626667 18.346667l42.666667-15.36a85.333333 85.333333 0 0 1 75.946666 8.106666 233.813333 233.813333 0 0 0 31.573334 18.346667 85.333333 85.333333 0 0 1 45.226666 61.866667l7.253334 42.666666a42.666667 42.666667 0 0 0 42.666666 35.84h98.133334a42.666667 42.666667 0 0 0 42.666666-35.84l7.253334-42.666666a85.333333 85.333333 0 0 1 45.226666-61.866667 233.813333 233.813333 0 0 0 31.573334-18.346667 85.333333 85.333333 0 0 1 75.946666-8.106666l42.666667 15.36a42.666667 42.666667 0 0 0 49.066667-18.346667l49.493333-85.333333a42.666667 42.666667 0 0 0-10.24-54.186667zM512 640a128 128 0 1 1 128-128 128 128 0 0 1-128 128z"
            p-id="2202" fill="#707070"></path>
      </svg>
    </div>
    <div v-if="tc" class="tc" style="background: white">
      <h1>123</h1>
    </div>
  </div>
  <div class="fixed input">
    <input ref="searchval" @keyup="search" @blur="noneSearchData" @click="showSearchData">
    <div class="sites">
      <el-radio v-model="site" label="百度" @click="showSearchData">百度</el-radio>
      <el-radio v-model="site" label="谷歌" @click="showSearchData">谷歌</el-radio>
      <el-radio v-model="site" label="必应" @click="showSearchData">必应</el-radio>
    </div>
    <div v-if="searchI" class="searchL">
      <div v-for="item in searchData" :key="item">
        <div>{{ item }}</div>
      </div>
    </div>
  </div>
  <div class="fixed imageFrom">
    <a :href="image['from']" target="_blank">背景图来源 wallhaven</a>
  </div>
</template>

<script>
export default {
  name: "Index",
  data() {
    return {
      image: {
        "from": "https://wallhaven.cc/w/e7ek7k",
        "url": "https://w.wallhaven.cc/full/e7/wallhaven-e7ek7k.jpg"
      },
      tc: false,
      site: "百度",
      searchI: false,
      searchData: []
    }
  },
  created() {
    document.title = "搜索"
  },
  methods: {
    showSetings() {
      this.tc = !this.tc
    },
    search() {
      let text = this.$refs.searchval.value
      console.log(text)
      if (text !== "") {
        console.log(text)
        let data = [1, 2, 3, 4, 5, 6, 7]
        this.searchData = data
      } else {
        document.getElementsByClassName("searchL")[0].style.display = "none"
      }
      this.searchI = true
    },
    noneSearchData() {
      this.searchI = false
    },
    showSearchData() {
      let text = this.$refs.searchval.value
      if (text !== "") {
        this.searchI = true
      }
    }
  },
}
</script>

<style scoped>
.background {
  height: 100%;
  object-fit: cover;
  width: 100%
}

.fixed {
  position: fixed;
  right: 0;
  left: 0;
  margin: 0 auto;
}

.rightTop {
  position: fixed;
  top: 20px;
  right: 20px;
  display: flex;
}

.rightTop svg {
  height: 35px;
  width: 100%;
}

.rightTop > div {
  padding: 0 4px;
  cursor: pointer;
}

.input {
  top: 20%;
  width: 30%;
  margin: 0 auto;
}

.sites {
  display: flex;
  justify-content: space-evenly;
  margin-top: 20px;
  color: black;
  cursor: pointer;
}

.sites :deep(span.el-radio__label) {
  background: white;
  border-radius: 30px;
  padding: 2px 14px;
  font-size: 15px;
}

.sites :deep(span.el-radio__input) {
  display: none;
}

.searchL {
  margin-top: 20px;
  background: white;
  border-radius: 15px;
  padding: 20px;
  display: block;
}

.tc {
  position: fixed;
  top: 63px;
  right: 28px;
}

.input input {
  text-align: center;
  width: 100%;
  height: 50px;
  outline: none;
  border-radius: 50px;
  border: none;
  font-size: 24px;
}

.imageFrom {
  bottom: 30px;
  width: 500px;
  margin: 0 auto;
  text-align: center;
  cursor: pointer;
}

.imageFrom a {
  color: white;
  text-decoration: none;
}

@media all and (max-width: 790px) {
  .input {
    width: 90%;
  }
}
</style>