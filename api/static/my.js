new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  data: {
    obj: null,
    faces: ["🤔", "😊", "🤪"],
    relations: [['ふむふむ'], ['にこにこ'], ['あはあは']],
    loader: "",
    url: "",
  },
  mounted: function (){
    this.obj = document.querySelector("#obj");
  },
  methods: {
    sendImage: function(e) {
      // 規定の送信処理をキャンセル(画面遷移などしない)
      e.preventDefault();
      this.loader = 'loading5';

      // 送信データの準備
      const formData = new FormData();
      const obj_file = this.obj.files[0];  // ファイル内容を詰める
      formData.append("obj", obj_file);  // ファイル内容を詰める

      const param = {
        method: "POST",
        body: formData
      }

      // アップロードする
      fetch("/lookat", param)
        .then((res)=>{
          return( res.json() );
        })
        .then((json)=>{
          this.url = URL.createObjectURL(obj_file);
          if (json.kashiko[0] == "") {
            this.relations[0] = "";
          } else {
            this.relations[0] = json.kashiko;
          }
          if (json.warui[1] == "") {
            this.relations[1] = "";
          } else {
            this.relations[1] = json.warui;
          }
          this.relations[2] = [""];
          // 通信が成功した際の処理
        })
        .catch((error)=>{
          // エラー処理
        });
    },
  }
});
