import globals from "globals";
import pluginJs from "@eslint/js";
import pluginVue from "eslint-plugin-vue";

export default [
  {
    files: ["**/*.{js,mjs,cjs,vue}"],
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
        EVALEX_TRUSTED: "writable",  // Change to writable if you need to modify it
        CONSOLE_MODE: "readonly",
        EVALEX: "readonly",
        SECRET: "readonly",
      },
    },
  },
  pluginJs.configs.recommended,
  ...pluginVue.configs["flat/essential"],
];
