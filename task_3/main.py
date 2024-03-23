def get_product_category_pairs(spark: SparkSession, p_df, c_df, pc_df):
    pcp = p_df.join(pc_df, p_df.product_id == pc_df.product_id, 'inner') \
        .join(c_df, pc_df.category_id == c_df.category_id, 'inner') \
        .select(p_df.product_name, c_df.category_name)

    pwc = p_df.join(pc_df, p_df.product_id == pc_df.product_id, 'left_anti') \
        .select(p_df.product_name)

    result_df = pcp.union(pwc.withColumn('category_name', col('product_name')))

    return result_df