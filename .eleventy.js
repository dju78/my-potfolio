module.exports = function(eleventyConfig) {
    // Passthroughs to simply copy these files to the output dir
    eleventyConfig.addPassthroughCopy("src/images");
    eleventyConfig.addPassthroughCopy("src/styles.css");
    eleventyConfig.addPassthroughCopy("src/script.js");
    eleventyConfig.addPassthroughCopy("src/admin");
    eleventyConfig.addPassthroughCopy("papers");
    eleventyConfig.addPassthroughCopy({ "public": "/" });

    // Returns the first `count` sentences of rendered HTML content as plain text,
    // for a short always-visible summary above a collapsible full-text block.
    eleventyConfig.addFilter("excerpt", (html, count = 2) => {
        const text = String(html || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
        const sentences = text.split(/(?<=[.!?])\s+(?=[A-Z(])/);
        return sentences.slice(0, count).join(" ").trim();
    });

    return {
        dir: {
            input: "src",
            output: "_site"
        }
    };
};
