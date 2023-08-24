import styles from "./Section.module.css";


function Section({children, title}) {
    return (
        <>
        <h1>{title}</h1>
        <div className={styles.section}>
        {children}
        </div>
        </>
    );
}

export default Section;
