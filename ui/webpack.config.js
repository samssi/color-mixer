const HtmlWebpackPlugin = require("html-webpack-plugin");

const htmlPlugin = new HtmlWebpackPlugin({
    template: "./src/index.html",
    filename: "index.html"
});

module.exports = {
    entry: "./src/index.js",

    output: {
        path: __dirname + '/dist',
        filename: 'index_bundle.js'
      },
      
    module: {
        rules: [
            { 
              test: /\.js$/, 
              exclude: /node_modules/,
              loader: ["babel-loader"]
            },
            {
              test: /\.css$/i, 
              use: ['style-loader', 'css-loader']
            }
        ]
    },
    plugins: [htmlPlugin]
}