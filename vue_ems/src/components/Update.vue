<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    update Emp info:
                </h1>
                <form>
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">id:</td>
                            <td valign="middle" align="left" v-model="id">{{$route.params.id}}</td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">name:</td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="name" v-model="emp_name"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">photo:</td>
                            <td valign="middle" align="left"><input type="file" name="photo" ref="photo"/></td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">salary:</td>
                            <td valign="middle" align="left"><input type="text" class="inputgri" name="salary"
                                                                    value="20000" v-model="salary"/></td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">age:</td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="age" value="20" v-model="age"/>
                            </td>
                        </tr>
                    </table>
                    <p>
                        <el-button @click="update_emp">更新提交</el-button>

                    </p>
                </form>
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
        name: "Update",
        data() {
            return {
                id: "",
                emp_name: "",
                salary: "",
                age: "",
                img: "",
                emp_obj: "",


            }
        },
        methods: {
            find() {
                let emp_id = this.$route.params.id;
                this.$axios.get("http://127.0.0.1:8000/api/employee/" + emp_id + "/").then(response => {
                    console.log(response.data.results);
                    this.emp_obj = response.data.results;
                    this.emp_name = this.emp_obj.emp_name;
                    this.salary = this.emp_obj.salary;
                    this.age = this.emp_obj.age;
                    this.img = this.emp_obj.img;
                }).catch(error => {
                })
            },


            update_emp() {
                let e_id = this.$route.params.id;
                console.log(e_id)
                console.log(this.$refs.photo.files[0]);
                let file = this.$refs.photo.files[0];
                let formdata = new FormData();
                formdata.append("emp_name", this.emp_name);
                formdata.append("salary", this.salary);
                formdata.append("age", this.age);
                formdata.append("img", file);

                console.log(formdata)
                this.$axios({
                    url: "http://127.0.0.1:8000/api/employee/" + e_id + `/`,
                    method: "put",
                    data: formdata,
                    headers: {"content-type": "multipart/form-data"},
                }).then(response => {
                    console.log(response.data.message);
                    if (response.data) {
                        this.$message({
                            message: "恭喜你，更新成功",
                            duration: 1000,
                            type: "success",
                        });
                        this.$router.push("/index");
                    }
                }).catch(error => {
                    this.$message({
                        message: "更新失败",
                        duration: 1000,
                        type: "fail",
                    });
                })
            }
        },
        created() {
            this.find()
        }
    }
</script>
<style scoped>
</style>
