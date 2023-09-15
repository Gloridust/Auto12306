# Auto12306

一个简单的12306抢票程序，让大学生有家可归。

## 在开始之前

这个程序使用了Selenium库来模拟浏览器行为，你需要安装Selenium并下载对应浏览器的驱动程序（如ChromeDriver）。

安装Selenium并下载对应浏览器的驱动程序是使用Selenium进行自动化测试的基本步骤。以下是安装Selenium以及下载Chrome浏览器驱动程序的步骤：

**1. 安装Python：** 如果你尚未安装Python，请从Python官方网站（<https://www.python.org/>）下载并安装最新版本的Python。在安装时，请勾选"Add Python to PATH"选项，以确保Python可在命令行中使用。

**2. 安装Selenium：** 在命令行中运行以下命令来安装Selenium：

```
pip install selenium
```

**3. 下载Chrome浏览器：** 如果你还没有安装Google Chrome浏览器，请从官方网站（<https://www.google.com/chrome/>）下载并安装它。

**4. 下载Chrome浏览器驱动程序（ChromeDriver）：** 你需要下载与你的Chrome浏览器版本相匹配的ChromeDriver。以下是下载和设置ChromeDriver的步骤：

   a. 首先查看你的Chrome浏览器版本。你可以在Chrome的地址栏中输入`chrome://settings/help`来查看当前版本。

   b. 访问ChromeDriver下载页面：<https://sites.google.com/chromium.org/driver/>

   c. 下载与你的Chrome版本匹配的ChromeDriver版本。确保选择正确的版本，下载后将它解压缩到一个目录中。

**5. 配置ChromeDriver路径：** 将ChromeDriver的路径添加到系统的环境变量中，或者在代码中指定ChromeDriver的路径。在上面的Python示例中，你需要将`'path_to_chromedriver'`替换为你ChromeDriver的实际路径。

完成以上步骤后，你就可以运行使用Selenium编写的Python程序，自动化执行Web操作，例如模拟用户登录和抢票。

请注意，Selenium是一个强大的工具，但也要小心使用，确保遵守网站的使用政策和法律法规。
