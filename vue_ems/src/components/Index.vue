<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        {{ nowDate }}
                        <br/>

                        <a href="javascript:;" @click="quit">安全退出</a>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    欢迎{{user_msg}}
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="(emp,index) in emp_list" :key="emp.id">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img :src="emp.img" style="height: 60px;"></td>
                        <!--                        <td>{{emp.img}}</td>-->
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>


                        <td>
<!--                            <a href="javascript:;" @click="update(emp.id)"> 更新员工</a>-->
                            <el-button><router-link :to="'/update/'+emp.id ">更新</router-link></el-button>
                            <el-button><a href="javascript:;" @click="del_emp(emp.id)">删除员工</a></el-button>

                        </td>
                    </tr>

                </table>
                <p>
                    <el-button>
                        <router-link to="/add">添加员工</router-link>
                    </el-button>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
        export default {
            name: "Index",
            data() {
                return {
                    user_msg: "",
                    emp_list: [],
                }
            },

            methods:{
                quit(){
                    sessionStorage.removeItem("user");
                    this.$router.push("/login");
                },

                findALLEmp(){
                    this.$axios.get("http://127.0.0.1:8000/api/employee/").then(response=>{
                        this.emp_list = response.data.results;
                    }).catch(error=>{

                    })
                },
                formatDate() {
                    let date = new Date();
                    let year = date.getFullYear(); // 年
                    let month = date.getMonth() + 1; // 月
                    let day = date.getDate(); // 日
                    let week = date.getDay(); // 星期
                    let weekArr = [ "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" ];
                    let hour = date.getHours(); // 时
                    hour = hour < 10 ? "0" + hour : hour; // 如果只有一位，则前面补零
                    let minute = date.getMinutes(); // 分
                    minute = minute < 10 ? "0" + minute : minute; // 如果只有一位，则前面补零
                    let second = date.getSeconds(); // 秒
                    second = second < 10 ? "0" + second : second; // 如果只有一位，则前面补零
                    this.nowDate = `${year}/${month}/${day} ${hour}:${minute}:${second} ${weekArr[week]}`;
                },


                del_emp(id) {
                    this.$axios({
                        url: "http://127.0.0.1:8000/api/employee/",
                        method: "delete",
                        params: {
                            id: id,
                        }
                    }).then(response => {
                        console.log(response);
                        this.findALLEmp();
                    })
                },
            },

            created() {
                let username = sessionStorage.getItem("user");
                if (username) {
                    this.user_msg = username;
                } else {
                    this.$message.error("对不起，请登录");
                    this.$router.push("/login");
                }
                this.findALLEmp();
                this.formatDate()
            },

        }
</script>

<style scoped>

</style>
