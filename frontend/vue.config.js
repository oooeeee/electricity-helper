module.exports = {
  publicPath: '/static',
  runtimeCompiler: true,
  pluginOptions: {
    svg: {
      inline: {}, // Pass options to vue-svg-loader
      data: {}, // Pass options to url-loader
      sprite: {}, // Pass options to svg-sprite-loader
      external: {} // Pass options to file-loader
    }
  },
}
