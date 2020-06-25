// 主题切换功能
function theme_change() {
    // 切换字内容
    var button = document.getElementById('theme_change');
    var pattern = new RegExp('暗黑系', 'i');
    if (pattern.test(button.innerHTML)){
        button.innerHTML = "光明系";
    } else{
        button.innerHTML = "暗黑系";
    }
    // 切换主题
    document.body.classList.toggle('dark-theme');
};
