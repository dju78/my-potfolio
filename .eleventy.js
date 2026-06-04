module.exports = function(eleventyConfig) {
    // Passthroughs to simply copy these files to the output dir
    eleventyConfig.addPassthroughCopy("src/images");
    eleventyConfig.addPassthroughCopy("src/styles.css");
    eleventyConfig.addPassthroughCopy("src/script.js");
    eleventyConfig.addPassthroughCopy("src/admin");
    eleventyConfig.addPassthroughCopy("papers");
    eleventyConfig.addPassthroughCopy("public");

    return {
        dir: {
            input: "src",
            output: "_site"
        }
    };
};
