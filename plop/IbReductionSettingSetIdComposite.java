
// IbReductionSettingSetId.java
import jakarta.persistence.Embeddable;
import java.io.Serializable;
import java.util.Objects;

@Embeddable
public class IbReductionSettingSetId implements Serializable {
    private String whoField;
    private String whoValue;

    public IbReductionSettingSetId() {}

    public IbReductionSettingSetId(String whoField, String whoValue) {
        this.whoField = whoField;
        this.whoValue = whoValue;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        IbReductionSettingSetId that = (IbReductionSettingSetId) o;
        return Objects.equals(whoField, that.whoField) &&
               Objects.equals(whoValue, that.whoValue);
    }

    @Override
    public int hashCode() {
        return Objects.hash(whoField, whoValue);
    }
}

// IbReductionSettingSet.java
import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Entity
public class IbReductionSettingSet {

    @EmbeddedId
    private IbReductionSettingSetId id;

    @OneToMany(mappedBy = "ibReductionSettingSet", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<IbReductionSetting> settings = new HashSet<>();

    public IbReductionSettingSet() {}

    public IbReductionSettingSet(IbReductionSettingSetId id) {
        this.id = id;
    }

    public IbReductionSettingSetId getId() {
        return id;
    }

    public void setId(IbReductionSettingSetId id) {
        this.id = id;
    }

    public Set<IbReductionSetting> getSettings() {
        return settings;
    }

    public void addSetting(IbReductionSetting setting) {
        settings.add(setting);
        setting.setIbReductionSettingSet(this);
    }

    public void removeSetting(IbReductionSetting setting) {
        settings.remove(setting);
        setting.setIbReductionSettingSet(null);
    }
}

// IbReductionSetting.java
import jakarta.persistence.*;

@Entity
@Table(uniqueConstraints = @UniqueConstraint(columnNames = {"ibReductionSettingSet_id", "what"}))
public class IbReductionSetting {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String what;

    private String unit;

    private String value;

    @ManyToOne
    @JoinColumns({
        @JoinColumn(name = "whoField", referencedColumnName = "whoField"),
        @JoinColumn(name = "whoValue", referencedColumnName = "whoValue")
    })
    private IbReductionSettingSet ibReductionSettingSet;

    public IbReductionSetting() {}

    public IbReductionSetting(String what, String unit, String value) {
        this.what = what;
        this.unit = unit;
        this.value = value;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getWhat() {
        return what;
    }

    public void setWhat(String what) {
        this.what = what;
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public IbReductionSettingSet getIbReductionSettingSet() {
        return ibReductionSettingSet;
    }

    public void setIbReductionSettingSet(IbReductionSettingSet ibReductionSettingSet) {
        this.ibReductionSettingSet = ibReductionSettingSet;
    }
}
