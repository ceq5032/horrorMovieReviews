module.exports = function (eleventyConfig){
    eleventyConfig.addPassthroughCopy("_src/_includes");
    eleventyConfig.addPassthroughCopy("_src/css/style.css");
    eleventyConfig.addPassthroughCopy("_src/images");
    eleventyConfig.addPassthroughCopy("_src/script/script.js");
    return{
        dir: {
            input:"_src",
            output: "_site",
            pathPrefix: "/horrorMovieReviews/"
        },
    };
};

